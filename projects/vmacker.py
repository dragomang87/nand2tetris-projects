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


FUNCTION COMMANDS

call function m
    - saves the current segment -> changes the segments adress to the end of their current size
    - takes m entries from the stack and puts them in the *new* argument segment
    - needs to make a label and "pass" it to the function to the function for the return call
        -> use THIS and THAT? one contains the chain of calls and the other tha chain of returns
        -> use static?
        -> use actual labels, eg (file.caller.callee.i)?
      I would pass it to argument or local, but this was not mentioned
      in the first example in II.2.3
    - jump to the function label

function name n
    - creates n entries in the local segments
    - uses the argument and local segment
    - writes the result in the stack, convention: a push to the stack must happen before the return call
        (but the function pushes to the stack all the time to do computation with argument and local,
         how do you check that the function did not leave too much or too little?)
    - returns to the provided label
    - create a label for the call

questions:
    - where do we store the chain of positions of the segments?
    - how to know which index of THIS and THAT the function has? maybe a whole array of segments locations and labels are stored in THIS and THAT


compiler safety features
    after a call, count the sum of push and pops to make sure the leftovers is at least one return value (some working stakck might be leftover on top of the return value
    need to keep a array of sums as long as the call chain

"""

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
# IMPLEMENTATION - SETUP AND NOTES
###############################################################################

# INPUT FILE
import sys

# Check if input file is given
if len(sys.argv) == 1:
    print(
        f"no input file provided\n"
        f"please give a text input file "
        f"(it will be treated as Hack assembly text file)",
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
        f"it will still be treated as Hack assembly text file"
        )
else:
    asm_filename = f"{vm_filename[:-3]}.asm"



# COMPILE VARIABLES

# The filename is used for label names
# Clean vm_filename from slashes that interefere with asm code
clean_filename = vm_filename.replace('/','_')

# We use dictionaries to produce code and use them as functions
# We split the dictionaries in
#   the VM  dictionary: contains mapping of actual VM code
#   the ASM dictionary: contains mapping of helper code

ASM = {}
VM = {}

# Some labels used in ASM code, function calls, etc
# are not global but unique label to the specific
# instance of the ASM code, call, etc
# So we keep track of how many of these labels are produced
# to give them a unique value using an instance index

ASM['instance_label_index'] = 0
instance_label = lambda: "instance_label_{ASM['instance_label_index']}"


# COMPILE NOTES

# We add some safety feature
# We clear registers and memory to 0 once they have been used/freed
# To distinguish these operations from needed assembly code
# we distinguish these operations by  marking them with a comment, e.g.
#   'M = 0                   // optional safety feature"
#   'D = 0                   // optional safety feature"
# instead of just
#   'M = 0"
#   'D = 0"
# If D is used to jump (comparisons or if-goto commands)
# then we leave D as it is instead of inntroducing
# state dependent behaviour (D=0 only when the jump is not made

###############################################################################
# IMPLEMENTATION - STACK
###############################################################################

# Predefined LIST with predefined location,
# we access by shifting a pointer up and down
# StackPointer = SP = 0
# Stack Base address RAM[SP] = RAM[0] = 256
# SP always points to the next where to push
# (the next "free" address)

ASM['push stack'] = (
        f"\n// ASM['push stack'] (from D)"
        f"\n@SP"
        f"\nA M = M + 1"
        f"\nA   = A - 1"
        f"\n  M = D"
        f"\n D  = 0             // optional safety feature"
        ) # 4+1 lines

ASM['push value'] = lambda i: (
        f"\n// ASM['push value']({i})"
        f"\n@{i}"
        f"\n D  = A"
        + ASM['push stack']
        ) # 6+1 lines

ASM['push ram'] = lambda i: (
        f"\n// ASM['push ram']({i})"
        f"\n@{i}"
        f"\n D  = M"
        + ASM['push stack']
        ) # 6+1 lines

ASM['pop stack'] = (
        f"\n// ASM['pop stack'] (to D)"
        f"\n@SP"
        f"\nA M = M - 1"
        f"\n D  = M"
        f"\n  M = 0             // optional safety feature"
        ) # 3+1 lines

ASM['pop sum'  ] = (
        f"\n// ASM['pop sum'] (to D)"
        f"\n@SP"
        f"\nA M = M - 1"
        f"\n D  = D + M"
        f"\n  M = 0             // optional safety feature"
        ) # 3+1 lines

ASM['pop sub'  ] = (
        f"\n// ASM['pop sub'] (to D)"
        f"\n@SP"
        f"\nA M = M - 1"
        f"\n D  = D - M"
        f"\n  M = 0             // optional safety feature"
        ) # 3+1 lines

ASM['move stack' ] = (
        f"\n// ASM['move stack']"
        f"\n// D = destination"
        # Like pop, but D contains the destination address
        # Implementation:
        #   - D can store address + value
        #   - the address is recovered with D - value
        # Steps
        #   A = a1      M = v       D = a2
        #   A = a1      M = v       D = a2 + v
        #   A = a2      M = ?       D = a2 + v
        #   A = a2      M = v       D = a2 + v
        # Accumulate destination and value in D
        #     A = source (stack), M == value
        #     D = destination + value, M == value
        #     A = destination, D == destination + value
        #     M = value = D - A
        f"\n// A = stack, M = value"
        f"\n@SP"
        f"\nA M = M - 1"
        f"\n// D = destination + value"
        f"\n D  = D + M"
        f"\n// A = destination, M = ?"
        f"\nA   = D - M"
        f"\n// A = destination, M = value"
        f"\n  M = D - A"
        f"\n D  = 0         // optional safety feature"
        f"\n@SP             // optional safety feature"
        f"\nA   = M         // optional safety feature"
        f"\n  M = 0         // optional safety feature"
        ) # 5+4 lines total

ASM['delete stack'] = (
        f"\n// ASM['delete stack']"
        f"\n@SP                 // optional safety feature"
        f"\nA M = M - 1         // optional safety feature"
        f"\n  M = 0             // optional safety feature"
        )

# Safety feature: discard stack by setting it to zero
# (instead of just moving the pointer and leaving the data there)
# Logic:
#   - use "while loop" style instead of "for loop" style
#   - while loop runs at least once, but has simpler assembly
#   - to avoid loosing data in the first run
#     we add one entry to the stack
#     (just SP++, no need to put a value in SP first
#      it likely already zero and is deleted anyway in the first run)
#   - nothing happens to the stack if D >= SP
ASM['delete stack to D'] = lambda instance_label: (
        f"\n// ASM['delete stack to D'] (until address D)"
        f"\n// (clear to zero until address D included)"
        f"\n// START optional safety feature"
        f"\n@SP                 // go to stack pointer"
        f"\n  M = M + 1         // add one entry to SP, one is always deleted"
        f"\n D  = M - D         // turn D into a counter of entries to clear"
        f"\n(asm_delete_stack_label.{clean_filename}.{instance_label})  // loop start"
        + ASM['delete stack'] + # 3 lines
        f"\n D  = D - 1         // decrement counter"
        f"\n@asm_delete_stack_label.{clean_filename}.{instance_label}      // point to clearing"
        f"\nD; JGT              // loop jump if counter >= 1"
        f"\n// END   optional safety feature"
        f"\n//@SP               // Alternative unsafe code"
        f"\n//  M = D + 1       // Alternative unsafe code"
        ) # 12 lines # 2 lines unsafe

# Implementation with zero of SP instead of SP--
# Downside: it has one more instruction in the loop
# Logic:
#   - use "while loop" style instead of "for loop" style
#   - while loop runs at least once, but has simpler assembly
#   - to avoid loosing data if there is nothing to do
#       - clear the current SP address
#         this might/will be zero on first entry
#         and is not part of the stack
#       - decrease the stack
#       - on exit do SP++
#   - if D >= SP then nothing happens
'''
ASM['delete stack to D'] = lambda instance_label: (
        f"\n// ASM['clear stack'] (until address D)"
        f"\n// (clear to zero until address D included)"
        f"\n// START optional safety feature"
        f"\n@SP                 // go to stack pointer"
        f"\n D  = M - D         // find how many entries need clearing"
        f"\n(asm_clear_stack_label.{clean_filename}.{instance_label})     // enter clearing one value"
        f"\n// SP -= 1, go back to SP+1, then delete"
        f"\n@SP                 // ⎫ clear current stack (might be zero already) and move up"
        f"\nA M = M - 1         // ⎟ and reduce the count of cleared entries,"
        f"\nA   = A + 1         // ⎬ repetitive for the first entry,"
        f"\n  M = 0             // ⎟ but needed because the code"
        f"\n D  = D - 1         // ⎭ is always executed at least once (easier implementation)"
        f"\n@asm_clear_stack_label.{clean_filename}.{instance_label}      // point to clearing"
        f"\nD; JGE              //   jump to clearing if there is more to clear"
        #f"\n@SP                 //   go to stack pointer"
        #f"\n  M = M + 1         //   move stack back up"
        f"\n// END   optional safety feature"
        f"\n//@SP               // Alternative unsafe code"
        f"\n//  M = D + 1       // Alternative unsafe code"
        ) # 12 lines # 2 lines unsafe
'''

###############################################################################
# IMPLEMENTATION - OPERATIONS
###############################################################################

# CONVENTIONS
# (mentioned in nand2tetris I and omitted in II.1)
#   false =  0
#   true  = -1
#   y     = last element of the stack
#   x     = second last element of the stack

# OPERATIONS
#   add: x + y
#   sub: x - y
#   neg: -y
#   eq : x == 0 (I think here it's y)
#   gt : x > y
#   lt : x < y
#   and: x and y
#   or : x or y
#   not: not y



# IMPLEMENTATIONS

# ARITHMETICS
#   add: x + y
#   sub: x - y
#   neg: -y
VM['add'] = (
        f"\n// VM add"
        + ASM['pop stack'] +
        f"\nA   = A - 1"
        f"\n  M = M + D"
        f"\n D  = 0             // optional safety feature"
        )
VM['sub'] = (
        f"\n// VM sub"
        + ASM['pop stack'] +
        f"\nA   = A - 1"
        f"\n  M = M - D"
        f"\n D  = 0             // optional safety feature"
        )
VM['neg'] = (
        f"\n// VM neg"
        f"\n@SP"
        f"\nA   = M - 1"
        f"\n  M = -M"
        )

# BOOLEANS
#   and: x and y
#   or : x or y
#   not: not y
VM['and'] = (
        f"\n// VM and"
        + ASM['pop stack'] +
        f"\nA   = A - 1"
        f"\n  M = M & D"
        f"\n D  = 0             // optional safety feature"
        )
VM['or'] = (
        f"\n// VM or"
        + ASM['pop stack'] +
        f"\nA   = A - 1"
        f"\n  M = M | D"
        f"\n D  = 0             // optional safety feature"
        )
VM['not'] = (
        f"\n// VM not"
        f"\n@SP"
        f"\nA   = M - 1"
        f"\n  M = !M"
        )


# COMPARISONS
#   eq : x == 0 (I think here it's x == y)
#   gt : x > y
#   lt : x < y

comparisons = {
        'eq': "EQ",
        'ne': "NE",
        'lt': "LT",
        'le': "LE",
        'gt': "GT",
        'ge': "GE",
        }

# Implementation:
# It is not possible to directly assing to A, D or M
# the value of a comparison
# therefore a jump must be used that requires a local label
# therefore this label needs an index
for comparison in comparisons:
    VM[comparison] = lambda instance_label, comparison=comparison: (
        f"\n// VM {comparison}"
        + ASM['pop stack'] +
        f"\nA   = A - 1"
        # Compute the difference
        f"\n D  = M - D"
        # Default x to the comparison being true
        f"\n  M = -1"
        # Point to skipping the comparison being false
        f"\n@compare_label.{clean_filename}.{comparison}.{instance_label}"
        # If the comparison is true skip setting it to false
        f"\nD; J{comparisons[comparison]}"
        # If the comparison was false and no skip happened, set it to false
        f"\n@SP"
        f"\nA   = M - 1"
        f"\n  M = 0"
        # Create the label to jump to if condition is true
        f"\n(compare_label.{clean_filename}.{comparison}.{instance_label})"
        ) # 11+2 lines (one label)





###############################################################################
#IMPLEMENTATION - ARRAY SEGMENTS
###############################################################################

# Segments:
#   local   : LCL  = 1
#   argument: ARG  = 2
#   this    : THIS = 3
#   that    : THAT = 4
#   temp    : 5 (fixed size to 8 values)

# Free registers:
#   R13
#   R14
#   R15

location = {
        'local'   : 'LCL ', # 1, #
        'argument': 'ARG ', # 2, #
        'this'    : 'THIS', # 3, #
        'that'    : 'THAT', # 4, #
        'temp'    : '5   ',
        'address' : 'R15 ',
        'return'  : 'R14 ',
        }

segment_max = {
        # 0:256 = 0:2**8 are standard registers and static
        # 2**14:2**15 is the screen buffer
        # the stack and the segments can overlap
        'local'   : 2**14 - 2**8,
        'argument': 2**14 - 2**8,
        'this'    : 2**14 - 2**8,
        'that'    : 2**14 - 2**8,
        # Non array segments have different maxima
        'temp'    : 8,              # 5:12
        'constant': 2**15,          # any value of A instructions, 2**15:2**16 are C instruction
        'pointer' : 2,
        'static'  : 2**8 - 2**4,    # range 16:256 = 2**4:2**8
        }

# segment[i] = RAM[SEGMENT + i]

VM['fetch'] = {}
VM['push'] = {}
VM['pop' ] = {}

for segment in ['local', 'argument', 'this', 'that', 'temp']:
    VM['fetch'][segment] = lambda i, segment=segment: (
            f"\n// ASM['address']['{segment}']({i})"
            f"\n// A = {segment} + {i} = source"
            f"\n@{location[segment]}"
            f"\n D  = " + ("A" if segment=="temp" else "M") +
            f"\n@{i}"
            f"\nA   = D + A"
            f"\n D  = M"
            f"\n M  = 0         // optional safety feature"
            ) # 5+1 lines

    VM['push'][segment] = lambda i, segment=segment: (
            f"\n// VM push {segment} {i}"
            f"\n// A = {segment} + {i} = source"
            f"\n@{location[segment]}"
            f"\n D  = " + ("A" if segment=="temp" else "M") +
            f"\n@{i}"
            f"\nA   = D + A"
            f"\n D  = M"
            f"\n M  = 0         // optional safety feature"
            + ASM['push stack'] # 4+1 lines
            ) # 9+2 lines

    VM['pop' ][segment] = lambda i, segment=segment: (
            f"\n// VM pop {segment} {i}"
            f"\n// D = {segment} + {i} = destination"
            f"\n@{location[segment]}"
            f"\n D  = " + ("A" if segment=="temp" else "M") +
            f"\n@{i}"
            f"\n D  = D + A"
            + ASM['move stack'] # 5+4 lines
            ) # 9+4 lines total



# If doing a push and pop in sequence
# maybe we can do better than 18+5
# by skipping the stack


# Implementation 2:
#   - get destination
#   - store in R15
#   - get source value
#   - get destination and put value
ASM['move'] = lambda from_segment, i, to_segment, j: (
        f"\n// VM push " + from_segment + " {i} = source"
        f"\n// VM pop  " + to_segment   + " {j} = destination"
        f"\n// ASM['move']({from_segment}, {i}, {to_segment}, {j})"
        f"\n// R15 = D = destination"   # 6 lines
        f"\n@{location[to_segment]}"
        f"\n D  = M"
        f"\n@{i}"
        f"\n D  = D + A"
        f"\n@R15"
        f"\n  M = D"
        f"\n// D = source value"   # 5+1 lines
        f"\n@{location[from_segment]}"
        f"\n D  = M"
        f"\n@{i}"
        f"\nA   = D + A"
        f"\n D  = M"
        f"\n  M = 0         // optional safety feature"
        f"\n// destination = source value"   # 3+4 lines
        f"\n@R15"
        f"\nA   = M"
        f"\n  M = D"
        f"\n D  = 0         // optional safety feature"
        f"\n@R15            // optional safety feature"
        f"\nA   = M         // optional safety feature"
        f"\n  M = 0         // optional safety feature"
        ) # 14+5 lines total instead of 18+5

'''

# Implementation 3:
#   - get destination
#   - store in R15
#   - get source value
#   - get destination and put value
ASM['move'] = lambda from_segment, i, to_segment, j: (
        f"\n// VM push " + from_segment + " {i} = source"
        f"\n// VM pop  " + to_segment   + " {j} = destination"
        f"\n// ASM['move']({from_segment}, {i}, {to_segment}, {j})"
        f"\n// D = value from source"   # 6 lines
        f"\n@{i}"
        f"\n D  = A"
        f"\n@{location[from_segment]}"
        f"\n  M = M + D"
        f"\nA   = M"
        f"\n D  = M"
        f"\n// D = value + destination" # 3 lines
        f"\n@{location[to_segment]}"
        f"\n D  = D + M"
        f"\n@{i}"
        f"\n D  = D + A"
        f"\n// A = source, M = value, D = destination + value" # 2 lines
        f"\n@{location[from_segment]}"
        f"\nA   = M"
        f"\n// A = destination, M = value" # 2 lines
        f"\nA   = D - M"
        f"\n  M = D - A"
        f"\n// restore source segment" # 4 lines
        f"\n@{i}"
        f"\n D  = A"
        f"\n@{location[from_segment]}"
        f"\n  M = 0         // optional safety feature"
        f"\n  M = M - D"
        f"\n D  = 0         // optional safety feature"
        ) # 17+2 lines total instead of 18+5

# Implementation 4:
#   - get source
#   - get source value
#   - get destination
#   - then pop as above
# If instead we try
#   - get destination
#   - get source
#   - add value to destination
# we don't have enough registers to do it
# getting the destination and then trying to add the source value
ASM['move'] = lambda from_segment, i, to_segment, j: (
        f"\n// VM push " + from_segment + " {i} = source"
        f"\n// VM pop  " + to_segment   + " {j} = destination"
        f"\n// ASM['move']({from_segment}, {i}, {to_segment}, {j})"
        f"\n// SP -> value"   # 8 lines
        f"\n@{location[from_segment]}"
        f"\n D  = M"
        f"\n@{i}"
        f"\nA   = D + A"
        f"\n D  = M"
        f"\n@SP"
        f"\nA   = M"
        f"\n  M = D"
        f"\n// D = destination" # 4 lines
        f"\n@{location[to_segment]}"
        f"\n D  = M"
        f"\n@{i}"
        f"\n D  = D + A"
        # Accumulate destination and value in D
        #     A = source (stack), M == value"
        #     D = destination + value, M == value"
        #     A = destination, D == destination + value"
        #     M = value = D - A"
        f"\n// A = source, M = value, D = destination + value" # 3 lines
        f"\n@SP"
        f"\nA   = M"
        f"\n D  = D + M"
        f"\n// A = destination, M = value" # 2 lines
        f"\nA   = D - M"
        f"\n  M = D - A"
        f"\n@{location[from_segment]}           // optional safety feature"
        f"\n D  = M         // optional safety feature"
        f"\n@{i}            // optional safety feature"
        f"\nA   = D + A     // optional safety feature"
        f"\n D  = 0         // optional safety feature"
        f"\n  M = 0         // optional safety feature"
        ) # 14+6 lines total instead of 18+5


# Implementation 1:
#   - get source
#   - get source value
#   - get destination
#   - then pop as above
# If instead we try
#   - get destination
#   - get source
#   - add value to destination
# we don't have enough registers to do it
# getting the destination and then trying to add the source value
ASM['move'] = lambda from_segment, i, to_segment, j: (
        f"\n// VM push " + from_segment + " {i} = source"
        f"\n// VM pop  " + to_segment   + " {j} = destination"
        f"\n// ASM['move']({from_segment}, {i}, {to_segment}, {j})"
        f"\n// D = value from source"   # 5 lines
        f"\n@{location[from_segment]}"
        f"\n D  = M"
        f"\n@{i}"
        f"\nA   = D + A"
        f"\n D  = M"
        f"\n// D = value + destination" # 3 lines
        f"\n@{location[to_segment]}"
        f"\n D  = D + M"
        f"\n@{i}"
        f"\n D  = D + A"
        # Accumulate destination and value in D
        #     A = source (stack), M == value"
        #     D = destination + value, M == value"
        #     A = destination, D == destination + value"
        #     M = value = D - A"
        f"\n// A = source, M = value, D = destination + value" # 4 lines
        f"\n@{location[from_segment]}"
        f"\n D  = M"
        f"\n@{i}"
        f"\nA   = D + A"
        f"\n// A = destination, M = value" # 2 lines
        f"\nA   = D - M"
        f"\n  M = D - A"
        f"\n@{location[from_segment]}           // optional safety feature"
        f"\n D  = M         // optional safety feature"
        f"\n@{i}            // optional safety feature"
        f"\nA   = D + A     // optional safety feature"
        f"\n D  = 0         // optional safety feature"
        f"\n  M = 0         // optional safety feature"
        ) # 14+6 lines total instead of 18+5

'''

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

# POINTER

pointer = {0: 'THIS', 1: 'THAT'}

VM['pop' ]['pointer'] = lambda i: (
        f"\n// VM pop pointer {i}"
        + ASM['pop stack'] +    # 3+1 lines
        f"\n@{pointer[i]}"
        f"\n  M = D"
        f"\n D  = 0             // optional safety feature"
        ) # 5+2 lines

VM['push']['pointer'] = lambda i: (
        f"\n// VM push pointer {i}"
        + ASM['push ram'](pointer[i])     # 6+1 lines
        ) # 6+1 lines


# STATIC

# Set the name of the ASM variable for static for this file
static = f"static.{clean_filename}"

VM['push']['static'] = lambda i: (
        f"\n// VM push static ({static}) {i}"
        + ASM['push ram']("{static}.{i}")
        )

VM['pop']['static'] = lambda i : (
        f"\n// VM pop  static ({static}) {i}"
        + ASM['pop stack'] +        # 3+1 lines
        f"\n@{static}.{i}"
        f"\n  M = D"
        f"\n D  = 0             // optional safety feature"
        ) # 5+2 lines


# CONSTANT

VM['push']['constant'] = lambda i: (
        f"\n// VM push constant {i}"
        + ASM['push value'](i)     # 6+1 lines
        ) # 6+1 lines


###############################################################################
# IMPLEMENTATION - BRANCHING
###############################################################################

# Dictionary to store VM labels to make sure they are not defined twice
# 'label <name>' should not appear twice with the same name in VM code
vm_labels = {}

#!!! Are VM labels file independent??? TODO

VM['label'] = lambda label: (
        f"\n// VM label {label}"
        f"\n(vm_label.{clean_filename}.{label})"
        ) # 1 ASM line, 0 HACK lines


VM['goto' ] = lambda label: (
        f"\n// VM goto {label}"
        f"\n@vm_label.{clean_filename}.{label}"
        f"\nJMP"
        ) # 2 lines

VM['if-goto'] = lambda label: (
        f"\n// VM goto {label}"
        + ASM['pop stack'] +    # 3+1 lines
        f"\n@vm_label.{clean_filename}.{label}"
        f"\nD; JMP"
        ) # 5+2 lines


# If a comparison happens just before 'if-goto'
# then we can save 8 lines
# because comparisons and jumps are one operation in machine code
#   push      :  9+2 ASM lines
#   comparison: 11+1 ASM lines
#   if-goto   :  5+2 lines

ASM['if'] = {}
ASM['if push'] = {}
for comparison in comparisons:
    ASM['if'][comparison] = {}
    ASM['if'][comparison]["stack"] = lambda label, comparison=comparison: (
            f"\n// ASM['if']['{comparison}']"
            f"\n// point stack to x and put it in D"
            f"\n@SP"
            f"\n  M = M - 1"
            f"\nA M = M - 1"
            f"\n D  = M" # x
            f"\n M  = 0         // optional safety feature"
            f"\n// point stack to y and compute the difference"
            f"\nA   = A + 1"
            f"\n D  = D - M" # x - y
            f"\n M  = 0         // optional safety feature"
            # Prepare jump label
            f"\n@vm_label.{clean_filename}.{label}"
            # Conditional jump
            f"\nD; J{comparisons[comparison]}"
            ) # 8+2 lines instead of 16+3


for segment in ['local', 'argument', 'this', 'that', 'temp']:
    ASM['if'][segment   ] = {}
    ASM['if']['pointer' ] = {}
    ASM['if']['static'  ] = {}
    ASM['if']['constant'] = {}
    for comparison in comparisons:
        ASM['if'][segment][comparison] = lambda label, i, segment=segment, comparison=comparison: (
                f"\n// A = {segment} + {i} = source"
                f"\n@{location[segment]}"
                f"\n D  = " + ("A" if segment=="temp" else "M") +
                f"\n@{i}"
                f"\nA   = D + A"
                f"\n D  = M"
                f"\n M  = 0         // optional safety feature"
                f"\n@SP"
                f"\nA M = M - 1"
                f"\n D  = M - D"
                f"\n M  = 0         // optional safety feature"
                # Prepare jump label
                f"\n@vm_label.{clean_filename}.{label}"
                # Conditional jump
                f"\nD; J{comparisons[comparison]}"
                ) # 10+2 lines instead of 25+5
    ASM['if']['pointer' ][comparison] = lambda label, i, segment=segment, comparison=comparison: (
            f"\n@{pointer[i]}"
            f"\n D  = M"
            f"\n@SP"
            f"\nA M = M - 1"
            f"\n D  = M - D"
            f"\n M  = 0         // optional safety feature"
            # Prepare jump label
            f"\n@vm_label.{clean_filename}.{label}"
            # Conditional jump
            f"\nD; J{comparisons[comparison]}"
            ) # 7+2 lines
    ASM['if']['static'  ][comparison] = lambda label, i, segment=segment, comparison=comparison: (
            f"\n@{static}.{i}"
            f"\n D  = M"
            f"\n@SP"
            f"\nA M = M - 1"
            f"\n D  = M - D"
            f"\n M  = 0         // optional safety feature"
            # Prepare jump label
            f"\n@vm_label.{clean_filename}.{label}"
            # Conditional jump
            f"\nD; J{comparisons[comparison]}"
            ) # 7+2 lines
    ASM['if']['constant'][comparison] = lambda label, i, segment=segment, comparison=comparison: (
            f"\n@{i}"
            f"\n D  = A"
            f"\n@SP"
            f"\nA M = M - 1"
            f"\n D  = M - D"
            f"\n M  = 0         // optional safety feature"
            # Prepare jump label
            f"\n@vm_label.{clean_filename}.{label}"
            # Conditional jump
            f"\nD; J{comparisons[comparison]}"
            ) # 7+2 lines





###############################################################################
# IMPLEMENTATION - BRANCHING
###############################################################################


function_label = lambda name: f"{clean_filename}." + name.replace('/','_')

VM['call'] = lambda name, n_arguments, instance_label: (
        f"\n// VM call {name} {n_arguments}"
        # Make sure the number of arguments is at least 1
        # (convention says that the return value is in ARG[0])
        + (
        f"\n@SP"
        f"\n  M = M + 1" if n_arguments == 0 else "")
        + ASM['push value'](f"return_label.{function_label(name)}.{instance_label}")
        + ASM['push ram']("LCL" )
        + ASM['push ram']("ARG" )
        + ASM['push ram']("THIS")
        + ASM['push ram']("THAT") +
        # A == SP
        f"\n// function LCL = SP"
        f"\n D  = M"
        f"\n@LCL"
        f"\n  M = D"
        f"\n// function ARG = SP - n_frame - n_arguments = SP - 5 - {n_arguments}"
        f"\n@5"
        f"\n D  = D - A"
        # Now the number of arguments is at least 1
        f"\n@{min(n_arguments,1)}"
        f"\n D  = D - A"
        f"\n@ARG"
        f"\n  M = D"
        f"\n D  = 0             // optional safety feature"
        f"\n@function_label.{function_label(name)}"
        f"\nJMP"
        f"\n(return_label.{function_label(name)}.{instance_label})"
        )


def vm_function(name, n_locals):
    return (
        f"\n// VM function {name} {n_locals}"
        f"\n(function_label.{function_label(name)})"
        f"\n@{n_locals}"
        f"\n D  = A"
        f"\n@SP"
        f"\n  M = M + D"
        )

VM['function'] = vm_function


def vm_return(instance_label):
    return (
        f"\n// VM return START"
        f"\n// Save the return value to argument[0],"
        f"\n// which is the top of the stack after return"
        + VM['pop']["argument"](0) +   # 9 + 1 lines
        f"\n// Clear the stack until LCL[0]"
        f"\n@LCL"
        f"\n D  = M"
        + ASM['delete stack to D'](instance_label + ".local") +     # 12 lines
        # SP points to calleeLCL - 1 -> callerTHAT
        # Make the stack skip the saved frame
        # (we can still return to the saved frame with LCL)
        f"\n// Skip the saved frame and clear until and point to ARG[1]"
        f"\n@5"
        f"\n D  = A"
        f"\n@SP"
        f"\n  M = M - D"                # SP -> calleeLCL - 6 = before the caller return address
        f"\n@ARG"
        f"\n D  = M + 1"
        + ASM['delete stack to D'](instance_label + ".argument") +     # 12 lines
        # LCL still point to after the saved frame
        f"\n// Return to saved frame and recover THAT"
        f"\n@LCL"
        f"\nA M = M - 1"        # RAM[LCL] = calleeLCL - 1 -> callerTHAT
        f"\n D  = M"
        f"\n  M = 0             // optional safety feature"
        f"\n@THAT"
        f"\n  M = D"
        f"\n// Return to saved frame and recover THIS"
        f"\n@LCL"
        f"\nA M = M - 1"        # RAM[LCL] = calleeLCL - 2 -> callerTHIS
        f"\n D  = M"
        f"\n  M = 0             // optional safety feature"
        f"\n@THIS"
        f"\n  M = D"
        f"\n// Return to saved frame and recover ARG"
        f"\n@LCL"
        f"\nA M = M - 1"        # RAM[LCL] = calleeLCL - 3 -> callerARG
        f"\n D  = M"
        f"\n  M = 0             // optional safety feature"
        f"\n@ARG"
        f"\n  M = D"
        f"\n// Return to saved frame and recover LCL"
        f"\n// keep the sum of both LCL in D to return to frame"
        # Start
        #   A = 0
        #   D = 0
        #   RAM[LCL] = a1 + 1
        #   RAM[a1]  = a2
        #
        # End:
        #   LCL = a2
        #   A or D = a1
        #
        # Option 1: 6 lines
        #   A = LCL
        #   ADM = M - 1: RAM[LCL] = A = D = a1, M == a2  (A = M mandatory first steps to do anything)
        #   D = M + D = a1 + a2
        #   A = LCL, M == a1
        #   M = RAM[LCL] = D - M = a2, A == LCL
        #   A = D - M = a1
        #
        # Option 2: 9 lines
        #   // Store LCL in R15 and go to it, 4 lines
        #   @LCL
        #    DM = M - 1
        #   @R15
        #   A M = D
        #   // Recover LCL, 3 lines
        #    D  = M
        #   @LCL
        #     M = D
        #   // Return to frame using R15, 2 lines
        #   @R15
        #   A   = M
        #
        f"\n@LCL"
        f"\nADM = M - 1"        # A = D = calleeLCL - 4 -> M = callerLCL
        f"\n D  = M + D"        # D = callerLCL + (calleeLCL - 4)
        f"\n@LCL"               # RAM[LCL] = M = (calleeLCL - 4)
        f"\n  M = D - M"        # RAM[LCL] = M = callerLCL
        f"\n// Return to saved frame and delete callerLCL"
        f"\nA   = D - M"        # A = (calleeLCL - 4) -> callerLCL
        f"\n  M = 0             // optional safety feature"
        f"\n// Recover caller's return address and jump"
        f"\nA   = A - 1"        # A = (calleeLCL - 5) -> return address
        f"\n D  = M"            # D = return address
        f"\n  M = 0             // optional safety feature"
        f"\nA   = D"            # A = return address
        f"\nJMP"
        f"\n// VM return END"
        )

VM['return'] = vm_return

###############################################################################
# Compile Functions
###############################################################################

# Compile logic:
#   - cannot check for which functions the returns are associated with
#     because there can be different return inside different branches
#   - without return cannot check which pop and push are inside the function



# Instance labels
# VM:
#   eq, lt, gt, ne, ge, le: 0 args
#   return, call          : 0 and 2 args
# ASM
#   'delete stack to D'

# Command syntax
#   1 word : add, sub, neg, or, and, not, eq, lt, gt, ne, ge, le, return
#   2 words: label, goto, if-goto
#   3 words: call, function, pop, push

# Command types:
#   strings     : add, sub, neg, or, and, not,
#   dict        : push, pop
#       function 1: push/pop segment
#   function 1  : return, label, goto, if-goto, eq, lt, gt, ne, ge, le
#   function 2  : function
#   function 3  : call

def compile_line(line):
    # Split all spaces
    split = line.split()
    # Get the command
    command = split[0]
    # Check for invalid command
    if command not in VM.keys():
        print("Valid commands:", VM.keys())
        raise SyntaxError(f"{command}: invalid command, must be one of the above")
    # Compile single command
    if len(split) == 1:
        if command in [
                'add', 'sub', 'neg',
                'or' , 'and', 'not',
                'eq' , 'lt' , 'gt' ,
                'ne' , 'ge' , 'le' ,
                'return',
                ]:
            return compile_single_command(command)
        # If it's one of the other commands then arguments are missing
        raise SyntaxError(f"{line} ...: missing one or two arguments")
    # Compile commands with one argument
    if len(split) == 2:
        if command in ['label', 'goto', 'if-goto']:
            return compile_branching(
                    command, split[1]
                    )
        if command in ['call', 'function', 'pop', 'push']:
            raise SyntaxError(f"{line} ...: missing one argument")
        # If other command then argument split[1] should not be there
        raise SyntaxError(f"{line}: {command} takes no arguments")
    # Compile commands with two arguments
    if len(split) == 3:
        if command in ['call', 'function']:
            return compile_function_and_call(
                    command, split[1], split[2]
                    )
        if command in ['push', 'pop']:
            return compile_segment(
                    command, split[1], split[2]
                    )
        if command in ['label', 'goto', 'if-goto']:
            raise SyntaxError(f"{line}: {command} takes only one argument")
        # If other command then argument split[1] and split[2] should not be there
        raise SyntaxError(f"{line}: {command} takes no arguments")
    # Reject commands with more arguments
    raise SyntaxError(
            f"{line}: wrong number of words for a VM command, max 3 words allowed."
            f"\n   An operation line   must contain a single keyword."
            f"\n   A segment   command must contain 2 keywords and a number."
            f"\n   A branching command must contain 1 keyword  and a label."
            f"\n   'call' and 'function' must be followed by 1 name and 1 positive integer."
            f"\n   A return command contains only 'return'."
            )


def compile_single_command(command):

    if isinstance(VM[command], str):
        return VM[command]
    else:
        ASM['instance_label_index'] += 1
        return VM[command](instance_label())


ASM['labels'] = {}
ASM['jumps' ] = {}
def compile_branching(command, label):

    # Make sure the label is valid
    try:
        float(label)
    except ValueError:
        pass
    else:
        # raise an error if it is a number
        raise ValueError(f"{command} {label}: label '{label}' "
                         f"in branching command {command} cannot be a number")
    # Keep track of defined and used labels
    if command == 'label':
        ASM['labels'][label] = True
        # Return the compiled code
        return VM['label'](label.replace("/", "_"))
    else:
        ASM['jumps' ][label] = True
        # Return the compiled code
        return VM[command](label.replace("/", "_"))


ASM['functions'] = {}
ASM['calls'    ] = {}
def compile_function_and_call(command, vm_name, n):

    # Make sure the vm_name is valid
    try:
        float(vm_name)
    except ValueError:
        pass
    else:
        # raise an error if the vm_name is a number
        raise SyntaxError(
                f"{command} {vm_name} {n}: name '{vm_name}' "
                f"in command {command} cannot be a number")
    # Make sure the third argument is a non-negative integer
    try:
        n = int(n)
        assert(n >= 0)
    except:
        raise ValueError(f"{command} {vm_name} {n}: {n} is negative")

    # Produce the ASM name of the function to track calls and definition
    asm_name = function_label(vm_name)

    # Compile 'call'
    if command == 'call':
        # Make sure the number of arguments is less than the maximum
        # (which would still run out of RAM)
        try:
            assert(n < segment_max['argument'])
        except:
            raise ValueError(
                    f"{command} {vm_name} {n}: the number of arguments "
                    f"must be below {segment_max['argument']}.\n"
                    f"At least one argument is needed to return the output.")
        # Make sure to have the function name in the list of function calls
        # and that it is called with always the same arguments
        if asm_name not in ASM['calls']:
            ASM['calls'][asm_name] = n
        elif not ASM['calls'][asm_name] == n:
            raise SyntaxError(
                    f"{command} {vm_name} {n}: function {vm_name} "
                    f"previously called with {ASM['calls'][asm_name]} "
                    f"arguments and now called with {n} arguments instead."
                    )
        # Compile the code
        ASM['instance_label_index'] += 1
        # Return the compiled code
        return VM['call'](vm_name, n, instance_label())

    # Compile 'function'
    if command == 'function':
        # Check if the function was defined already
        if asm_name in ASM['functions']:
            raise SyntaxError(f"function {vm_name} already defined")
        # Add the name to the list of defined functions
        # with the number of local variables to check for overflow
        ASM['functions'][asm_name] = True
        # Return the compiled code
        return VM['function'](vm_name, n)



def compile_segment(move, segment, i):

    # Make sure the segment is valid
    if segment not in VM[move].keys():
        print("Valid segments:", VM[move].keys())
        raise SyntaxError(
                f"{segment}: invalid segment, must be one of the above")
    # Make sure the index is a non-negative integer
    try:
        i = int(i)
        assert(i >= 0)
    except:
        raise SyntaxError(
                f"{i}: invalid index for any segment, "
                f"must be a non-negative integer")
    # Make sure the index is not too big
    if i >= segment_max[segment]:
        raise ValueError(
                f"{i}: outside of range for segment {segment}")
    # Return the compiled code
    return VM[move][segment](i)


def compile_double_line(line):
    return ""

###############################################################################
# COMPILATION FUNCTIONS
###############################################################################

def clean_line(line):
    # Remove comments
    line = line.split('//')[0]
    # Remove extra spaces
    return ' '.join(line.split())

def compile_vm_to_asm(vm_filename, asm_filename, debug=False):
    if debug: print(f"Compiling file {vm_filename} into {asm_filename}")
    # Compile
    with open( vm_filename, 'r') as virtual_machine, \
         open(asm_filename, 'w') as assembly:
        # Loop over lines
        for (line_number, line) in enumerate(virtual_machine, 1):
            # Remove comments
            line = clean_line(line)
            # Ignore empty lines
            if line == '': continue
            # Try to compile
            try:
                if debug: print(f"Compiling line {line_number}: '{line}'")
                assembly.write(compile_line(line))
            except Exception as e:
                raise Exception(
                    f"Compilation failed in line {line_number}"
                    ) from e

    # Final Warnings

    # Warn of undefined functions, unused arguments and argument overflow
    for function in ASM['calls']:
        if function not in ASM['functions']:
            # if ASM['functions'][function] fails then it was not defined
            import warnings
            warnings.warn(
                    f"function {function} was called but not defined",
                    SyntaxWarning)

    # Warn of used but undefined labels
    for jump in ASM['jumps']:
        try:
            ASM['labels'][jump]
        except:
            import warnings
            warnings.warn(
                    f"label {jump} was used but not defined",
                    SyntaxWarning)



###############################################################################
# COMPILE
###############################################################################



# Compile Hack virtual machine code to Hack assembly language
compile_vm_to_asm(vm_filename, asm_filename, debug=True)


