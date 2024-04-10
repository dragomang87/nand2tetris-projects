###############################################################################
# HACK Assembly Language Specification
###############################################################################

# All possible instructions are 16-bits instructions

# They describe
#   Registers and Memory
#   Branching
#   Variables
#   Iteration
#   Pointers
#   Input/Output
# Split into three types of instructions
#   A(ddress) instructions
#   L(abel) instructions (Label declarations)
#   C(omputation) instructions


###############################################################################
# TOOLS
###############################################################################

def clean_line(line):
    # purge comments
    line = line.split('//')[0]
    # purge white spaces
    return ''.join(line.split())


###############################################################################
# ADDRESSES
###############################################################################

# Hack Machine language is a sequence of 16-bit commands
#   commands starting with 0 are A(ddress) instructions
#   commands starting with 1 are C(computation) instructions
# Therefore addresses are 16-bit long but can only have 15-bit values

def compile_address(decimal):
    # get the binary form as string
    # [2:] strips the leading 0b... from the string
    bits = (bin(decimal))[2:]
    # pad to 16 bits (15 address + 1 control zero bit)
    return bits.zfill(16)


###############################################################################
# L(ABEL) INSTRUCTIONS (LABEL DECLARATIONS)
###############################################################################
#
# Assembly Syntax:
#   (LABEL)
#
# This instruction does not produce any machine code
# It assigns to LABEL the value of the program_counter
# of the next coming instruction,
# so that it can be used in A(ddress) instructions
#
# There are some default labels that do not need declaration
# To implement labels, we create a dictionary assigning addresses to labels
# We store these addresses already as compiled bitstrings
# To declare labels, we split compilation in two passes:
#   PASS 1 - count all instructions (program counter) but skip compilation,
#            when a label declaration is found assign the correct program counter
#            and store the label in the dictionary
#   PASS 2 - ingnore all label declarations and compile all
#            A(ddress) instructions, using the dictionary when needed,
#            and C(omputation) instructions

labels = {}

def parse_label_instruction(line):
    # check if the opening syntax ( parenthesis is missing
    # the parenthesis is checked by the code calling this function
    # so if this happens something might be wrong with this file
    if line[0] != '(' :
        raise RuntimeError(
            f"Hack assembly to machine language compiler {__file__}:\n"
            "line without leading ( passed to parse_label_instruction(...), "
            "there might be a problem with this compiler {__file__}"
            )
    # check if the closing syntax parenthesis ) is missing
    if (line[-1] != ')'):
        raise SyntaxError("(LABEL) declaration: missing trailing)")
    # remove the parentheses to get the label
    # ! notice that spaces are not removed and are left as part of the label !
    label = line[1:-1]
    # check if the label is a number
    try:
        float(label)
    # return the label otherwise
    except:
        return label
    # raise an error if it is a number
    else:
        raise ValueError("LABEL in (LABEL) declaration cannot be a number")


def compile_label_instruction(label, program_counter):
    # Convert the program counter integer to a bitstring address
    # and assign it as value to the given label in the given label dictionary
    # This is a bit different than compiling A and C instructions
    # because the machine code of Label instructions
    # depends on the position in the assembly file
    # therefore there is a part of the compilation,
    # which is figuring out this position,
    # that is done by the global parser
    # and is passed to the instruction compiler as arguments
    labels[label] = compile_address(program_counter)



###############################################################################
# A(DDRESS) INSTRUCTIONS
###############################################################################
#
# Assembly Syntax:
#   @<address>
#   @LABEL
#   @VARIABLE
# where
#   <address> is a 15bit integer
#   LABEL has a 15bit integer value assigned to it by L(abel) instructions
#   VARIABLE:
#       starting from address 16,
#       gets assigned a new free register address at the first encounter
#       and is mapped to the assigned values at the next encounter
#
# Variables do not need to exist from the beginning unlike labels,
# so a second pass is not needed,
# The '@next' variable, which is prohibited in assembly code,
# is used to keep track of what is the next free register

variables = {
    # store the next available address
    # cannot be called 'next' because it may be used by the assembly code
    # the parser will never interpret '@next' as a value so this entry is safe
    '@next'  : 16,
    'SP'     : '0000' '0000' '0000' '0000', #     0, #
    'LCL'    : '0000' '0000' '0000' '0001', #     1, #
    'ARG'    : '0000' '0000' '0000' '0010', #     2, #
    'THIS'   : '0000' '0000' '0000' '0011', #     3, #
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

def parse_compile_Ainstruction(line):
    # PARSE
    value = line[1:]
    # Check if empty
    if not value:
        raise SyntaxError("A(ddress) instruction: empty address")
    # Make sure there is only one @ at the beginning
    if value[0] == '@':
        raise SyntaxError('A(address) instruction: only one leading @ allowed')
    # COMPILE
    # Check if the address is a 15bit integer
    try:
        A = int(value)
        # Check that the address is not too big
        # The RAM size is 32KiB = 2**15 B
        if A >= 2**15:
            raise ValueError(
                    "A(ddress) instruction: "
                    "integer address provided "
                    "but it exceeds 15 bits (32768 or above)"
                    )
        # Compile A(ddress) to binary instruction as string
        A = compile_address(A)
    except ValueError as evalue:
        # Dissallow float values
        try:
            A = float(value)
        except:
            # check if it is a label
            if   value in labels:
                A = labels   [value]
            elif value in variables:
                A = variables[value]
            else:
                # Raise error if we are out of RAM for the new variable
                # The RAM is segmented in three memory chips
                #   16KiB for the RAM
                #    8KiB for the Screen
                #    1  B for the keyboard
                if variables['@next'] == 2**14:
                    raise MemoryError(
                        "A(ddress) instruction: "
                        "out of RAM for assembly variables, "
                        "label '" + value + "' reached address 2^14 "
                        "which enters Screen memory map"
                        )
                # Treat as new variable
                A = variables[value] = compile_address(variables['@next'])
                # Move future variables to next address
                variables['@next'] += 1
        else:
            # Raise error if float
            # (if we raise inside the try clause
            #  it will trigger creating a lable with float value)
            raise ValueError(
                    "A(ddress) instruction: float not allowed as address"
                    )

    return A + '\n'



###############################################################################
# C(OMPUTATION) INSTRUCTIONS
###############################################################################
#
# Assembly Syntax:
#   destination = computation; jump
#
# Hack machine language syntax:
#   1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3
#
#
# destination / d1 d2 d3:
#   any combination of A, D and M = RAM[A]
#   d1 = 1 if A is a destination, otherwise zero
#   d2 = 1 if D is a destination, otherwise zero
#   d3 = 1 if M is a destination, otherwise zero
#
# jump / j1 j2 j3:
#   jump:
#       JLT JGT: jump if computation result is less or greater than zero
#       JLE JGE: jump if computation result is less/greater or equal to zero
#       JEQ JNE: jump if computation result equal or not equal to zero
#       JMP or empty: unconditional jump or not jump
#   j1 j2 j3:
#       j1 = 1 if jump when computation result is less than zero,
#            0 otherwise
#       j2 = 1 if jump when computation result equals zero,
#            0 otherwise
#       j3 = 1 if jump when computation result is greater than zero,
#            0 otherwise

jumps = {
#   jump  : j1 j2 j3
    ''    : '000',
    'JLT' : '100',
    'JEQ' : '010',
    'JGT' : '001',
    'JLE' : '110', # JLT & JEQ
    'JNE' : '101', # JLT       & JGT
    'JGE' : '011', #       JEQ & JGT
    'JMP' : '111', # JLT & JEQ & JGT
    }

# computation / a c1 c2 c3 c4 c5 c6:
#   addressing: a = 0 if A is selected for computation,
#                   1 if M is selected for computation
#   operation: see dictionary below
#              for available operations on A and D (when a=0)
#              and the corresponding bitstrings c1 c2 c3 c4 c5 c6

computations = {
# computation : c1 c2 c3 c4 c5 c6
    '0'   : '101010',
    '1'   : '111111',
    '-1'  : '111010',
    'D'   : '001100',
    'A'   : '110000',
    '!D'  : '001101',
    '!A'  : '110001',
    '-D'  : '001100',
    '-A'  : '110011',
    'D+1' : '011111',
    '1+D' : '011111',
    'A+1' : '110111',
    '1+A' : '110111',
    'D-1' : '001110',
    '-1+D': '001110',
    'A-1' : '110010',
    '-1+A': '110010',
    'D+A' : '000010',
    'A+D' : '000010',
    'D-A' : '010011',
    '-A+D': '010011',
    'A-D' : '000111',
    '-D+A': '000111',
    'D&A' : '000000',
    'A&D' : '000000',
    'D|A' : '010101',
    'A|D' : '010101',
    }

def parse_Cinstruction(line):
    # Check if too many = signs
    # (do this by counting splits,
    #  we also save the splits for later)
    eq_split = line.split("=")
    if len(eq_split) > 2:
        raise SyntaxError("C(omputation) instruction: only one = sign allowed")
    # Check if too many ; signs
    # (do this by counting splits,
    #  we also save the splits for later)
    semicolon_split = line.split(";")
    if len(eq_split) > 2:
        raise SyntaxError("C(omputation) instruction: only one ; sign allowed")
    # Find = and ;
    eq        = line.find("=") + 1
    semicolon = line.find(";") + 1
    # Check if = comes before ;
    if (eq > semicolon) and semicolon:
        raise SyntaxError(
            "C(omputation) instruction: "
            "assignment symbol = cannot appear before jump delimiter ;"
            )
    # Parse computation-only instruction
    if not( eq or semicolon ):
        # Warn the user that the instruction ultimately does nothing
        import warnings
        warnings.warn(
            "C(omputation) instruction: no = or ; detected, "
            "this instruction will have no effect "
            "on register, memory or program counter",
            SyntaxWarning
            )
        destination, computation, jump = '', line, ''
    # Parse assignment-computation instruction
    elif eq and (not semicolon):
        destination, computation, jump = eq_split + ['']
    # Parse computation-jump instruction
    elif (not eq) and semicolon:
        destination, computation, jump = [''] + semicolon_split
    # Parse assignment-computation-jump instruction
    else:
        destination, computation, jump = [eq_split[0]] + eq_split[0].split(";")
    return destination, computation, jump



def compile_Cinstruction(destination, computation, jump):

    ###################################
    # DESTINATION
    ###################################

    # Determine the destination by simply checking the presence of A, D, M
    # and then removing them, however this for A, D, M to appear multiple times

    # Check if A destination is set
    if destination.find('A') == -1:
        A = '0'
    else:
        A = '1'
    destination = destination.replace("A",'')

    # Check if D destination is set
    if destination.find('D') == -1:
        D = '0'
    else:
        D = '1'
    destination = destination.replace("D",'')

    # Check if M destination is set
    if destination.find('M') == -1:
        M = '0'
    else:
        M = '1'
    destination = destination.replace("M",'')

    # Warn user if there are other characters than A, D and M in the assignment
    if destination:
        import warnings
        warnings.warn(
            "C(omputation) instruction: there are spurious characters "
            "in assignment (left side of =)",
            SyntaxWarning
            )

    # Final destination
    destination = A + D + M


    ###################################
    # JUMP
    ###################################

    # Simply use the dictionary,
    # if the string is not in jumps then it is not valid
    try:
        jump = jumps[jump]
    except:
        print(jumps.key())
        raise SyntaxError(
            "C(omputation) instruction: "
            "jump (right of ;) not recognised, "
            "only the jumps listed above are allowed"
            )


    ###################################
    # ADDRESSING
    ###################################
    # A or M addressing

    # Check if A is in the computation
    A = bool(computation.find('A') + 1)
    # Check if M is in the computation
    M = bool(computation.find('M') + 1)
    # It's an error to have both present
    if A and M:
        raise SyntaxError(
            "C(omputation) instruction: only one of A and M "
            "can present at the same time in computation "
            "between assignment and jump (between = and ;)"
            )
    # If only M is present then the addressing bit a is 1
    # then we use a trick to keep the operations dictionary compact:
    # once a=1 is set, the operations that can be done with M
    # are the same that can be done with A,
    # so we convert M to A in the computation string
    # and keep the operations dictionary more compact
    # by keeping only operations with A
    elif M:
        addressing = '1'
        computation = computation.replace('M','A')
    # If only A is present then the addressing bit a is 0
    else:
        addressing = '0'

    ###################################
    # OPERATION
    ###################################
    # remember that after parsing M we converted it to A,
    # so we only need to check for computations with A and D
    try:
        computation = computations[computation]
    except:
        print(computations.keys())
        raise SyntaxError(
            "C(omputation) instruction: operation not recognized, "
            "only the operations listed above are allowed"
            )

    ###################################
    # C INSTRUCTION
    ###################################

    # Put the instruction together
    return '111' + addressing + computation + destination + jump + '\n'



###############################################################################
# COMPILATION FUNCTIONS
###############################################################################

# PASS 1 - ASSEMBLY LABEL PASS
# Find all label declarations in Hack assembly code (*.asm)
def parse_asm_labels(asm_filename):
    # Reading labels pass
    with open(asm_filename, 'r') as assembly:
        # Set counter of the instruction sequence number
        program_counter = 0
        for (line_number, line) in enumerate(assembly, 1):
            # Remove spaces
            line = clean_line(line)
            # Ignore empty lines
            if not line:
                pass
            # Parse lines starting with '(' as label declarations
            elif line[0] == '(':
                try:
                    label = parse_label_instruction(line)
                    compile_label_instruction(label, program_counter)
                except Exception as e:
                    raise Exception(
                        f"Failed (LABEL) declaration in line {line_number}"
                        ) from e
            # Parse everything else as instructions
            # that increase the program counter
            else:
                program_counter +=1

# PASS 2 - HACK MACHINE CODE PASS
# Compile Hack assembly code (*.asm) to Hack machine language (*.hack)
def compile_asm_to_hack(asm_filename, hack_filename, debug=False):
    if debug: print(f"Compiling file {asm_filename} into {hack_filename}")
    with open( asm_filename, 'r') as assembly, \
         open(hack_filename, 'w') as machine:
        # Set counter of the instruction sequence number
        program_counter = 0
        # Loop over lines
        for (line_number, line) in enumerate(assembly, 1):
            # Remove spaces
            line = clean_line(line)
            if debug: print(f"Compiling line {line_number}: '{line}'")
            # Ignore empty lines
            if not line:
                pass
            # Parse and compile lines starting with '@' as A(ddress) instructions
            elif line[0] == '@':
                try:
                    instruction = parse_compile_Ainstruction(line)
                    # Increase program counter
                    program_counter += 1
                    # Write instruction to .hack file
                    machine.write(instruction)
                    if debug: print(instruction)
                except Exception as e:
                    raise Exception(
                        "A(ddress) instruction: "
                        f"compilation failed in line {line_number}"
                        ) from e
            # Ignore Label declarations which shoud have been processed already
            # resulting in the up-to-date labels dictionary
            elif line[0] == '(':
                pass
            # Parse and compile every other line as C(omputation) instructions
            else:
                try:
                    # Parse
                    destination, computation, jump = parse_Cinstruction(line)
                    if debug: print(
                            f"destination: {destination}, "
                            f"computation: {computation}, "
                            f"jump: {jump}"
                            )
                    # Compile
                    instruction = compile_Cinstruction(
                            destination,
                            computation,
                            jump,
                            )
                    # Increase program counter
                    program_counter +=1
                    # Write instruction to .hack file
                    machine.write(instruction)
                    if debug: print(instruction)
                except Exception as e:
                    raise Exception(
                        "C(omputation) instruction: "
                        f"compilation failed in line {line_number}"
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
asm_filename = sys.argv[1]



# OUTPUT FILE

# Generate output file with .hack extension
if asm_filename[-4:] != ".asm":
    hack_filename = asm_filename + '.hack'
    import warnings
    warnings.warn(
        f"Extension of input file {asm_filename} is not '.asm', "
        "it will still be treated as Hack assembly text file"
        )
else:
    hack_filename = asm_filename[:-4] + '.hack'


# COMPILE

# PASS 1 - parse labels in assembly code
# (dictionaries are mutable and passed by reference)
parse_asm_labels(asm_filename)

# PASS 2 - compile Hack assembly code to Hack machine language
compile_asm_to_hack(asm_filename, hack_filename, debug=True)




#def main():
#    print("Hello World!")
#
#if __name__ == "__main__":
#    compile_hack_asm()

