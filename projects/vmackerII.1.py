###############################################################################
# HACK Virtual Machine Language Specification
###############################################################################

"""
STACK
    Predefined LIST with predefined location,
    we access by shifting a pointer up and down
    StackPointer = SP = 0
    Stack Base address RAM[SP] = RAM[0] = 256
    SP always points to the next where to push
    (the next "free" address)


OPERATIONS ON STACK (Module II.1.2)
    y: last element of the stack
    x: second last element of the stack
    add: x + y
    sub: x - y
    neg: -y
    eq : x == 0 (I think here it's y)
    gt : x > y
    lt : x < y
    and: x and y
    or : x or y
    not: not y

MEMORY SEGMENTS (Module II.1.3)

Move:
    pop  segment i: pop from the stack into segment[i]
                    Exception: "pop  const i" not allowed
    push segment i: push the value of segment[i] into the stack

Segments:
    predefined ARRAYS with variable location
    we access by indexing from the location
    location/pointer stored in predefined location
    !We don't decide the location in this project!
    The location is provided as initial RAM state

    local   :
        poiter LCL = 1
        base address RAM[LCL]
        local[i] = RAM[LCL + i]
    argument:
        pointer ARG = 2
        base address RAM[ARG]
        arguments[i] = RAM[ARG + i]
    this    :
        poiter THIS = 3
        base address RAM[THIS]
        this[i] = RAM[THIS + i]
    that    :
        pointer THAT = 4
        base address RAM[THAT]
        that[i] = RAM[THAT + i]
    constant:
            const[i] = i (no need to actually store it)
    temp    :
        dedicated RAM locations 5 to 12
        i = 0..7
        temp[i] = RAM[5+i]
        fixed size to 8 values
    pointer :
        another fixed memory segment of size 2
        pointer[0] = RAM[THIS]
        pointer[1] = RAM[THAT]
Static:
    predefined ARRAY with predefined location
    static  :
        will be shared by all instances of the same objects
        it is compiled differently
        static[i] becomes an assembly variable, eg, static.i
        automatically stored by the compiler in RAM[16] and onwards
        might need to take care to never exceed RAM[255] for static

Helper command not part of the virtual machine (for now):
    D = *p with p a RAM address => D = RAM[p]
    *p = value => RAM[p] = value
    x++
    x--
"""



###############################################################################
# IMPLEMENTATION - NOTES
###############################################################################

# We use dictionaries to produce code and use them as functions
# We split the dictionaries in
#   the VM  dictionary: contains mapping of actual VM code
#   the ASM dictionary: contains mapping of helper code

ASM = {}
VM = {}

# We add some safety feature
# We clear registers and memory to 0 once they have been used/freed
# To distinguish these operations from needed assembly code
# we distinguish these operations by  marking them with a comment, e.g.
#   'M = 0 // optional safety feature"
#   'D = 0 // optional safety feature"
# instead of just
#   'M = 0"
#   'D = 0"


###############################################################################
# IMPLEMENTATION - STACK
###############################################################################

# Predefined LIST with predefined location,
# we access by shifting a pointer up and down
# StackPointer = SP = 0
# Stack Base address RAM[SP] = RAM[0] = 256
# SP always points to the next where to push
# (the next "free" address)

ASM['pop stack'] = (
        f"\n// ASM pop stack"
        f"\n@SP"
        f"\nA M = M - 1"
        f"\n D  = M"
        f"\n  M = 0 // optional safety feature"
        ) # 3+1 lines

ASM['push stack'] = (
        f"\n// ASM push stack"
        f"\n@SP"
        f"\nA M = M + 1"
        f"\nA   = A - 1"
        f"\n  M = D"
        f"\n D  = 0 // optional safety feature"
        ) # 4+1 lines

"""
ASM['push stack'] = (
        f"\n// ASM push stack"
        f"\n@SP"
        f"\nA   = M"
        f"\n  M = D"
        f"\n@SP"
        f"\n  M = M + 1"
        f"\n D  = 0 // optional safety feature"
        ) # 5+1 lines
"""


###############################################################################
# IMPLEMENTATION - OPERATIONS
###############################################################################

# y: last element of the stack
# x: second last element of the stack
# add: x + y
# sub: x - y
# neg: -y
# eq : x == 0 (I think here it's y)
# gt : x > y
# lt : x < y
# and: x and y
# or : x or y
# not: not y

# Load/Fetch
#   RAM = ..., x, y, *SP, ...

# M = y:
ASM['M = y'] = (
        f"\n@SP"
        # A points to SP - 1
        # !! SP is unchanged
        f"\nA   = M - 1"
        )

# M,D = x,y:
ASM['M,D = x,y'] = (
        # pop y to D
        ASM['pop stack'] +
        # A points to SP - 1
        # !! SP still points to y, not x
        f"\nA   = A - 1"
        )

# Arithmetic
#   add: x + y
#   sub: x - y
#   neg: -y
VM['add'] = (
        f"\n// VM add"
        + ASM['M,D = x,y'] +
        f"\n  M = M + D"
        f"\n D  = 0 // optional safety feature"
        )
VM['sub'] = (
        f"\n// VM sub"
        + ASM['M,D = x,y'] +
        f"\n  M = M - D"
        f"\n D  = 0 // optional safety feature"
        )
VM['neg'] = (
        f"\n// VM neg"
        + ASM['M = y'] +
        f"\n  M = -M"
        )

# Boolean
#   and: x and y
#   or : x or y
#   not: not y
VM['and'] = (
        f"\n// VM and"
        + ASM['M,D = x,y'] +
        f"\n  M = M & D"
        f"\n D  = 0 // optional safety feature"
        )
VM['or'] = (
        f"\n// VM or"
        + ASM['M,D = x,y'] +
        f"\n  M = M | D"
        f"\n D  = 0 // optional safety feature"
        )
VM['not'] = (
        f"\n// VM not"
        + ASM['M = y'] +
        f"\n  M = !M"
        )


# Comparison
#   eq : x == 0 (I think here it's x == y)
#   gt : x > y
#   lt : x < y
#
# It is not possible to directly assing to A, D or M
# the value of a comparison
# therefore a jump must be used that requires a local label
# therefore this label needs an index
comparisons = {
        "eq": "EQ",
        "ne": "NE",
        "lt": "LT",
        "le": "LE",
        "gt": "GT",
        "ge": "GE",
        }

ASM['comparisons_index'] = 0

for cmp in comparisons:
    VM[cmp] = lambda index: (
        f"\n// VM {cmp}"
        + ASM['M,D = x,y'] +
        # Compute the difference
        f"\n D  = M - D"
        # Default to the comparison being true
        f"\n  M = 1"
        # Point to skipping the comparison being false
        f"\n@ CMP.{index}"
        # If the comparison is true skip setting it to false
        f"\nD; J{comparisons[cmp]}"
        # If the comparison was false and no skip happened, set it to false
        f"\n@SP"
        f"\nA   = M - 1"
        f"\n  M = 0"
        # Create the label to jump to if condition is true
        f"\n(CMP.{index})"
        )





###############################################################################
#IMPLEMENTATION - ARRAY SEGMENTS
###############################################################################

segment_max = {
        # 0:2048 = 0:2**11 are standard registers, static and the stack
        # 2**14:2**15 is the screen buffer
        'local'   : 2**14 - 2**11,
        'argument': 2**14 - 2**11,
        'this'    : 2**14 - 2**11,
        'that'    : 2**14 - 2**11,
        # Non array segments have different maxima
        'temp'    : 8,              # 5:12
        'constant': 2**15,          # any value of A instructions, 2**15:2**16 are C instruction
        'pointer' : 2,
        'static'  : 2**8 - 2**4,    # range 16:256 = 2**4:2**8
        }

# segment[i] = RAM[SEGMENT + i]

# local   : LCL = 1
# argument: ARG = 2
# this    : THIS = 3
# that    : THAT = 4
# temp    : 5 (fixed size to 8 values)

location = {
        'local'   : 'LCL' , # 1, #
        'argument': 'ARG' , # 2, #
        'this'    : 'THIS', # 3, #
        'that'    : 'THAT', # 4, #
        'temp'    : '5'   ,
        'address' : 'R15' ,
        }

VM['push'] = {}
VM['pop' ] = {}

ASM['register'] = lambda register, segment, i: (
        f"\n// ASM {register} = {segment} + {i}"
        f"\n@{segment}"
        f"\n D  = M"
        f"\n@{i}"
        f"\n{register} = D + A"
        ) # 4 lines

# Temporary address variable
# Options:
#   @address
#   @R13
#   @R14
#   @R15
# The problem with using @address
# is that it takes away static memory.
# We store the choice of R13, R14 or R15
# in location['address']
#ASM['push address'] = (
#        f"\n// ASM push address"
#        f"\n@{location['address']}"
#        f"\nA   = M"
#        f"\n  M = D"
#        f"\n D  = 0 // optional safety feature"
#        )
#
#ASM['address'] = lambda register, segment, i: (
#        f"\n// ASM address = {segment} + {i}"
#        + ASM['register']("D", segment, i) +
#        f"\n@{location['address']}"
#        f"\n  M = D"
#        ) # 6 lines total

for segment in ['local', 'argument', 'this', 'that', 'temp']:
    VM['push'][segment] = lambda i: (
            f"\n// VM push {segment} {i}"
            + ASM['register']("A", segment,i) + # 4 lines, D = segment + i
            f"\n D  = M"
            + ASM['push stack']                 # 4+1 lines
            ) # 9+1 lines

    # pop  implementation with accumulation:
    # D can store address + value
    # and the address is recovered with D - value
    VM['pop' ][segment] = lambda i: (
            f"\n// VM pop {segment} {i}"
            + ASM['register']("D", segment,i) + # 4 lines, D = segment + i
            f"\n@SP"
            f"\nA M = M - 1"  # M = value
            f"\n D  = D + M"  # D = segment + i + value
            f"\nA   = D - M"  # A   = segment + i
            f"\n  M = D - A"  # M = value
            f"\n D  = 0     // optional safety feature"
            f"\n@SP       // optional safety feature"
            f"\nA   = M + 1 // optional safety feature"
            f"\n  M = 0     // optional safety feature"
            ) # 9+4 lines total
#    # pop  mplementation with @address:
#    # @address stores the address of "segment i"
#    VM['pop' ][segment] = lambda i: (
#            f"\n// VM pop {segment} {i}"
#            + ASM['address'](location[segment], i)  # 6 lines
#            + ASM['pop stack']                      # 3+1 lines
#            + ASM['push address'] +                 # 3+1 lines
#            f"\n@address // optional safety feature"
#            f"\n  M = 0 // optional safety feature"
#            ) # 12+4 lines total
#    # pop  mplementation changing location[segment]:
#    # We can add i to location[segment] and then subtract it again
#    VM['pop' ][segment] = lambda i: (
#            f"\n// VM pop  {segment} {i}"
#            f"\n@{i}"
#            f"\n D  = A"
#            f"\n@{segments[segment]}"
#            f"\n  M = M + D"
#            + ASM['pop stack'] +                    # 3+1 lines
#            f"\n@{segments[segment]}"
#            f"\nA   = M"
#            f"\n  M = D"
#            f"\n@{i}"
#            f"\n D  = A"
#            f"\n@{segments[segment]}"
#            f"\n  M = M - D"
#            f"\n D  = 0 // optional safety feature"
#            ) # 14+2 lines total
#    # pop  mplementation with @SP v1:
#    # @SP stores the address of "segment i"
#    VM['pop' ][segment] = lambda i: (
#            f"\n// VM pop  {segment} {i}"
#            f"\n@{i}"
#            f"\n D  = A"
#            f"\n@{segments[segment]}"
#            f"\n D  = M + D"               # D = segment i
#            f"\n@SP"
#            f"\nA M = M - 1"
#            f"\nA   = A + 1"
#            f"\n  M = D"                   # segment i in on top of the stack
#            f"\nA   = A - 1"
#            f"\n D  = M"                   # D = value
#            f"\nA   = A + 1"
#            f"\nA   = M"                   # A   = segment i
#            f"\n  M = D"
#            f"\n D  = 0     // optional safety feature"
#            f"\n@SP         // optional safety feature"
#            f"\nA   = M     // optional safety feature"
#            f"\n  M = 0     // optional safety feature"
#            f"\nA   = A - 1 // optional safety feature"
#            f"\n  M = 0     // optional safety feature"
#            ) # 13+5 lines total
#    # pop  mplementation with @SP v2:
#    # @SP stores the address of "segment i"
#    VM['pop' ][segment] = lambda i: (
#            f"\n// VM pop  {segment} {i}"
#            f"\n@{i}"                      #  1
#            f"\n D  = A"                   #  2
#            f"\n@{segments[segment]}"      #  3
#            f"\n D  = M + D"               #  4 D = segment i
#            f"\n@SP"                       #  5
#            f"\nA   = M"                   #  6
#            f"\n  M = D"                   #  7 segment i in on top of the stack
#            f"\nA   = A - 1"               #  8
#            f"\n D  = M"                   #  9 D = value
#            f"\nA   = A + 1"               # 10
#            f"\nA   = M"                   # 11
#            f"\n  M = D"                   # 12
#            f"\n D  = 0     // optional safety feature"
#            f"\n@SP"
#            f"\nA M = M - 1"
#            f"\n  M = 0     // optional safety feature"
#            f"\nA   = A 1 1 // optional safety feature"
#            f"\n  M = 0     // optional safety feature"
#            ) # 14+4 lines total


###############################################################################
#IMPLEMENTATION - SPECIAL SEGMENTS
###############################################################################

# constant: const[i] = i (no need to actually store it)
# pointer :
#     another fixed memory segment of size 2
#     pointer[0] = RAM[THIS]
#     pointer[1] = RAM[THAT]
# Static:
#     predefined ARRAY with predefined location
#     static  :
#         will be shared by all instances of the same objects
#         it is compiled differently
#         static[i] becomes an assembly variable, eg, static.i
#         automatically stored by the compiler in RAM[16] and onwards
#         might need to take care to never exceed RAM[255] for static

# CONSTANT

VM['push']['constant'] = lambda i: (
        f"\n// VM push constant {i}"
        f"\n@{i}"
        f"\n D  = A"
        + ASM['push stack']     # 4+1 lines
        ) # 6+1 lines

# POINTER

pointer = {0: 'THIS', 1: 'THAT'}

VM['pop' ]['pointer'] = lambda i: (
        f"\n// VM pop pointer {i}"
        + ASM['pop stack'] +    # 3+1 lines
        f"\n@{pointer[i]}"
        f"\n  M = D"
        f"\n D  = 0 // optional safety feature"
        ) # 5+2 lines
VM['push']['pointer'] = lambda i: (
        f"\n// VM push pointer {i}"
        f"\n@{pointer[i]}"
        f"\n D  = M"
        + ASM['push stack']     # 4+1 lines
        ) # 6+1 lines


# STATIC

static = "static"

def push_static(i):
    return (
        f"\n// VM push static ({static}) {i}"
        f"\n@{static}.{i}"
        f"\n D  = M"
        + ASM['push stack']
        )

VM['push']['static'] = push_static

def pop_static(i):
    return (
        f"\n// VM pop  static ({static}) {i}"
        + ASM['pop stack'] +        # 3+1 lines
        f"\n@{static}.{i}"
        f"\n  M = D"
        f"\n D  = 0 // optional safety feature"
        ) # 5+2 lines

VM['pop']['static'] = pop_static


###############################################################################
# HACK Assembly Language Specification
###############################################################################

# L(ABEL) INSTRUCTIONS (LABEL DECLARATIONS):
#   (LABEL)

# A(DDRESS) INSTRUCTIONS:
#   @<address>
#   @LABEL
#   @VARIABLE
# where VARIABLE gets a new free register address at the first encounter
# starting from address 16

# C(OMPUTATION) INSTRUCTIONS
#   destination = computation; jump
# destination: any combination of A, D and M = RAM[A]
# jump:
#   jump: JLT JGT JLE JGE JEQ JNE JMP or empty
# computation:
#   '0' '1' '-1'
#   'D' '!D' '-D'
#   'A' '!A' '-A'
#   'D+1' '1+D' 'D-1' '-1+D'
#   'A+1' '1+A' 'A-1' '-1+A'
#   'D+A' 'A+D' 'D-A' '-A+D' 'A-D' '-D+A'
#   'D&A' 'A&D' 'D|A' 'A|D'


"""
default_variables = {
    # store the next available address
    # cannot be called 'next' because it may be used by the assembly code
    # the parser will never interpret '@next' as a value so this entry is safe
    '@next'  : 16,
    'SP'     : '0000' '0000' '0000' '0000', #     0, #
    'LCL'    : '0000' '0000' '0000' '0001', #     1, #
    'ARG'    : '0000' '0000' '0000' '0010', #     2, #
    'THIS'   : '0000' '0000' '0000' '0011', #     3, #
    'THAT'   : '0000' '0000' '0000' '0100', #     4, #
    'THAT'   : '0000' '0000' '0000' '0100', #     4, #
    'SCREEN' : '0100' '0000' '0000' '0000', # 16384, #
    'KBD'    : '0110' '0000' '0000' '0000', # 24576, #
    'R0'     : '0000' '0000' '0000' '0000', #     0, #
    'R1'     : '0000' '0000' '0000' '0001', #     1, #
    'R2'     : '0000' '0000' '0000' '0010', #     2, #
    'R3'     : '0000' '0000' '0000' '0011', #     3, #
    'R4'     : '0000' '0000' '0000' '0100', #     4, #
    'R5'     : '0000' '0000' '0000' '0101', #     5, #
    'R6'     : '0000' '0000' '0000' '0110', #     6, #
    'R7'     : '0000' '0000' '0000' '0111', #     7, #
    'R8'     : '0000' '0000' '0000' '1000', #     8, #
    'R9'     : '0000' '0000' '0000' '1001', #     9, #
    'R10'    : '0000' '0000' '0000' '1010', #    10, #
    'R11'    : '0000' '0000' '0000' '1011', #    11, #
    'R12'    : '0000' '0000' '0000' '1100', #    12, #
    'R13'    : '0000' '0000' '0000' '1101', #    13, #
    'R14'    : '0000' '0000' '0000' '1110', #    14, #
    'R15'    : '0000' '0000' '0000' '1111', #    15, #
    }
"""

###############################################################################
# TOOLS
###############################################################################

def clean_line(line):
    # Remove comments
    line = line.split('//')[0]
    # Remove extra spaces
    return ' '.join(line.split())

###############################################################################
# Compile Functions
###############################################################################

def compile_line(line):
    # Split all spaces
    split = line.split()

    if len(split) == 1:
        return compile_operation(split[0])
    if len(split) == 3:
        return compile_segment(split[0], split[1], split[2])

    raise SyntaxError(f"{line}: wrong number of words."
                      "\nAn operation line must contain a single word."
                      "\nA segment line must contain 2 words and a number."
                      )


def compile_operation(operation):

    try:
        operation = VM[operation]
    except:
        print("Valid commands:", VM.keys())
        raise SyntaxError(f"{move}: invalid command, must be one of the above")

    if isinstance(operation, str):
        return operation
    else:
        ASM['comparisons_index'] += 1
        return operation(ASM['comparisons_index'])


def compile_segment(move, segment, i):

    try:
        move = VM[move]
    except:
        print("Valid commands:", VM.keys())
        raise SyntaxError(f"{move}: invalid command, must be one of the above")

    try:
        move_segment = move[segment]
    except:
        print("Valid operations:", move.keys())
        raise SyntaxError(f"{segment}: invalid segment, must be one of the above")

    try:
        i = int(i)
    except:
        raise SyntaxError(f"{i}: invalid segment index, must be an integer")

    if i >= segment_max[segment]:
        raise ValueError(f"{i}: outside of range for segment {segment}")

    return move_segment(i)



###############################################################################
# COMPILATION FUNCTIONS
###############################################################################

def compile_vm_to_asm(vm_filename, asm_filename, debug=False):
    if debug: print(f"Compiling file {vm_filename} into {asm_filename}")
    with open( vm_filename, 'r') as virtual_machine, \
         open(asm_filename, 'w') as assembly:
        # Loop over lines
        for (line_number, line) in enumerate(virtual_machine, 1):
            # Remove comments
            line = clean_line(line)
            if debug: print(f"Compiling line {line_number}: '{line}'")
            # Ignore empty lines
            if line == '':
                continue
            try:
                assembly.write(compile_line(line))
            except Exception as e:
                raise Exception(
                    f"Compilation failed in line {line_number}"
                    ) from e



###############################################################################
# COMPILER
###############################################################################

# INPUT FILE
import sys

# Check if input file is given
if len(sys.argv) == 1:
    print(
        "no input file provided\n"
        "please give a text input file "
        "(it will be treated as Hack assembly text file)",
        file=sys.stderr
        )
    sys.exit(1)

# Save input filename
vm_filename = sys.argv[1]



# OUTPUT FILE

# Generate output file with .hack extension
if vm_filename[-3:] != ".vm":
    asm_filename = f"{vm_filename}.asm"
    import warnings
    warnings.warn(
        f"Extension of input file {vm_filename} is not '.vm', "
        "it will still be treated as Hack assembly text file"
        )
else:
    asm_filename = f"{vm_filename[:-3]}.asm"


# COMPILE

# Set the name of the ASM variable for static for this file
static = f"static.{vm_filename}"

# Compile Hack virtual machine code to Hack assembly language
compile_vm_to_asm(vm_filename, asm_filename, debug=True)


