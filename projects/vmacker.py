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

"""
IMPLEMENTATION
    - intermediate pass to pointer logic?
    - dictionaries for segments
    - how to choose segment location?
    - stack lower bound 256? how to avoid operating on static?
    - stack upper bound? how to avoid operating on other segements
"""

ASM = {}
VM = {}




###############################################################################
# IMPLEMENTATION - STACK
###############################################################################

# Predefined LIST with predefined location,
# we access by shifting a pointer up and down
# StackPointer = SP = 0
# Stack Base address RAM[SP] = RAM[0] = 256
# SP always points to the next where to push
# (the next "free" address)

ASM["pop stack"] = (
        "\n// ASM pop stack"
        "\n@SP"
        "\nAM = M - 1"
        "\nD = M"
        # optional safety feature
        # (set stack to zero,
        #  instead of just abandoning it)
        "\nM = 0"
        )
ASM["push stack"] = (
        "\n// ASM push stack"
        "\n@SP"
        "\nA = M"
        "\nM = D"
        "\n@SP"
        "\nM = M + 1"
        # optional safety feature
        # (set register to zero,
        #  instead of just abandoning it)
        "\nD = 0"
        )


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
ASM["M = y"] = (
        "\n@SP"
        # A points to SP - 1
        # !! SP is unchanged
        "\nA = M - 1"
        )

# M,D = x,y:
ASM["M,D = x,y"] = (
        # pop y to D
        ASM["pop stack"] +
        # A points to SP - 1
        # !! SP still points to y, not x
        "\nA = A - 1"
        )

# Arithmetic
#   add: x + y
#   sub: x - y
#   neg: -y
VM["add"] = (
        "\n// VM add"
        + ASM["M,D = x,y"] +
        "\nM = M + D"
        "\nD = 0 "      # optional safety feature
        )
VM["sub"] = (
        "\n// VM sub"
        + ASM["M,D = x,y"] +
        "\nM = M - D"
        "\nD = 0 "      # optional safety feature
        )
VM["neg"] = (
        "\n// VM neg"
        + ASM["M = y"] +
        "\nM = -M"
        )

# Boolean
#   and: x and y
#   or : x or y
#   not: not y
VM["and"] = (
        "\n// VM and"
        + ASM["M,D = x,y"] +
        "\nM = M & D"
        "\nD = 0 "      # optional safety feature
        )
VM["or"] = (
        "\n// VM or"
        + ASM["M,D = x,y"] +
        "\nM = M | D"
        "\nD = 0 "      # optional safety feature
        )
VM["not"] = (
        "\n// VM not"
        + ASM["M = y"] +
        "\nM = !M"
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

ASM["comparisons_index"] = 0

for cmp in comparisons:
    VM[cmp] = lambda index: (
        "\n// VM " + cmp
        + ASM["M,D = x,y"] +
        # Compute the difference
        "\nD = M - D"
        # Default to the comparison being true
        "\nM = 1"
        # Point to skipping the comparison being false
        "\n@ CMP." + str(index) +
        # If the comparison is true skip setting it to false
        "\nD; J" + comparisons[cmp] +
        # If the comparison was false and no skip happened, set it to false
        "\n@SP"
        "\nA = M - 1"
        "\nM = 0"
        # Create the label to jump to if condition is true
        "\n(CMP." + str(index) + ")"
        # Point to the stack again
        # (by default it needs to be incremented after this operation)
        "\n@SP"
        )





###############################################################################
#IMPLEMENTATION - ARRAY SEGMENTS
###############################################################################

segment_max = {
        'local'   : 2**14 - 256,
        'argument': 2**14 - 256,
        'this'    : 2**14 - 256,
        'that'    : 2**14 - 256,
        'temp'    : 8,
        'constant': 2**15,
        'pointer' : 2,
        'static'  : 2**15,
        }

# segment[i] = RAM[SEGMENT + i]

# local   : LCL = 1
# argument: ARG = 2
# this    : THIS = 3
# that    : THAT = 4
# temp    : 5 (fixed size to 8 values)

segments = {
        'local'   : 'LCL' , # 1, #
        'argument': 'ARG' , # 2, #
        'this'    : 'THIS', # 3, #
        'that'    : 'THAT', # 4, #
        }

VM["push"] = {}
VM["pop" ] = {}

ASM["A"] = lambda segment, i: (
        "\n// ASM A(" + segment + "," + str(i) + ")"
        "\n@" + segment +
        "\nD = M"
        "\n@" + str(i) +
        "\nA = D + A"
        )
ASM["D"] = lambda segment, i: (
        ASM["A"](segment,i) +
        "\nD = M"
        )

ASM["value 0"] = (
        "\n@value"
        "\nM = 0"
        )

ASM["address 0"] = (
        "\n@address"
        "\nM = 0"
        )

ASM["push address"] = (
        "\n// ASM push address"
        "\n@address"
        "\nA = M"
        "\nM = D"
        "\nD = 0"      # optional safety feature
        )

ASM["address"] = lambda segment, i: (
        "\n// ASM address(" + segment + "," + str(i) + ")"
        "\n@" + segment +
        "\nD = M"
        "\n@" + str(i) +
        "\nD = D + A"
        "\n@address"
        "\nM = D"
        )

for segment in segments:
    VM["push"][segment] = lambda i: (
            "\n// VM push " + segment + " " + str(i)
            + ASM["D"](segments[segment], i)
            + ASM["push stack"]
            )

    VM["pop" ][segment] = lambda i: (
            "\n// VM pop "  + segment + " " + str(i)
            + ASM["address"](segments[segment], i)
            + ASM["pop stack"]
            + ASM["push address"]
            + ASM["address 0"]
            )

VM["push"]['temp'] = lambda i: (
        "\n// VM push temp " + str(i) +
        "\n@5"
        "\nD = A"
        "\n@" + str(i) +
        "\nA = D + A"
        "\nD = M"
        + ASM["push stack"]
        )

VM["pop" ]['temp'] = lambda i: (
        "\n// VM pop temp " + str(i) +
        "\n@5"
        "\nD = A"
        "\n@" + str(i) +
        "\nD = D + A"
        "\n@address"
        "\nM = D"
        + ASM["pop stack"]
        + ASM["push address"]
        + ASM["address 0"]
        )

###############################################################################
#IMPLEMENTATION - ARRAY SEGMENTS
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

VM["push"]["constant"] = lambda i: (
        "\n// VM push constant " + str(i) +
        "\n@" + str(i) +
        "\nD = A"
        + ASM["push stack"]
        )

# POINTER

pointer = {0: 'THIS', 1: 'THAT'}

VM["pop" ]["pointer"] = lambda i: (
        "\n// VM pop pointer " + str(i)
        + ASM["pop stack"] +
        "\n@" + pointer[i] +
        "\nM = D"
        "\nD = 0 "      # optional safety feature
        )
VM["push"]["pointer"] = lambda i: (
        "\n// VM push pointer " + str(i) +
        "\n@" + pointer[i] +
        "\nD = M"
        + ASM["push stack"]
        )


# STATIC

static = "static"

def push_static(i):
    return (
        "\n// VM push static (" + static + ") " + str(i) +
        "\n@" + static + "." + str(i) +
        "\nD = M"
        + ASM["push stack"]
        )

VM["push"]["static"] = push_static

def pop_static(i):
    return (
        "\n// VM pop  static (" + static + ") " + str(i)
        + ASM["pop stack"] +
        "\n@" + static + "." + str(i) +
        "\nM = D"
        "\nD = 0 "      # optional safety feature
        )

VM["pop"]["static"] = pop_static


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

    raise SyntaxError(line + ": wrong number of words."
                      "\nAn operation line must contain a single word."
                      "\nA segment line must contain 2 words and a number."
                      )


def compile_operation(operation):

    try:
        operation = VM[operation]
    except:
        print("Valid commands:", VM.keys())
        raise SyntaxError(move + ": invalid command, must be one of the above")

    if isinstance(operation, str):
        return operation
    else:
        ASM["comparisons_index"] += 1
        return operation(ASM["comparisons_index"])


def compile_segment(move, segment, i):

    try:
        move = VM[move]
    except:
        print("Valid commands:", VM.keys())
        raise SyntaxError(move + ": invalid command, must be one of the above")

    try:
        move_segment = move[segment]
    except:
        print("Valid operations:", move.keys())
        raise SyntaxError(segment + ": invalid segment, must be one of the above")

    try:
        i = int(i)
    except:
        raise SyntaxError(i + ": invalid segment index, must be an integer")

    if i >= segment_max[segment]:
        raise ValueError(i + ": outside of range for segment " + segment)

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
    asm_filename = vm_filename + '.asm'
    import warnings
    warnings.warn(
        f"Extension of input file {vm_filename} is not '.vm', "
        "it will still be treated as Hack assembly text file"
        )
else:
    asm_filename = vm_filename[:-3] + '.asm'


# COMPILE

# Set the name of the ASM variable for static for this file
static = "static." + vm_filename

# Compile Hack virtual machine code to Hack assembly language
compile_vm_to_asm(vm_filename, asm_filename, debug=True)


