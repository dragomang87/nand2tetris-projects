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
#   Labels
#   C(omputation) instructions


###############################################################################
# TOOLS
###############################################################################

def clean_line(line):
    # purge white spaces
    line = ''.join(line.split())
    # purge comments
    return line.split('//')[0]


###############################################################################
# ADDRESSES
###############################################################################

def compile_address(decimal):
    # get the binary form as string
    # [2:] strips the leading 0b... from the string
    bits = (bin(decimal))[2:]
    # pad to 16 bits (15 address + 1 control zero bit)
    return bits.zfill(16)


###############################################################################
# A INSTRUCTIONS
###############################################################################

def parse_compile_Ainstruction(line, labels):
    # PARSE
    value = line[1:]
    # check if empty
    if not value:
        raise ValueError("Empty A-instruction")
    # COMPILE
    try:
        # check if number
        A = int(value)
        # Check that the address is not too big
        if A >= 2**15:
            raise ValueError("Value of A-instruction exceeds 16 bits (65536 or above)")
        # COMPILE A INSTRUCTION
        # Convert to binary instruction as string
        A = compile_address(A)
    except ValueError as evalue:
        try:
            # check if existing lable
            A = labels[value]
        except KeyError as ekey:
            # raise KeyError("Label in A instruction not previously defined") from e
            try:
                A = float(value)
            except:
                # Treat as new variable
                A = labels[value] = compile_address(labels['@next'])
                labels['@next'] += 1
                if labels['@next'] == 2**14:
                    raise MemoryError("You have run out of RAM for variables (next variable would have address 2^16 which enters Screen memory map)")
            else:
                raise ValueError("Floats are not allowed in A-instruction")

    return A + '\n'



###############################################################################
# LABELS
###############################################################################

default_labels = {
    # store the next available address
    # cannot be called 'next' because it may be used by the assembly code
    # the parser will never interpret '@next' as a value so this entry is safe
    '@next'  : 16,
    'SP'     : '0000' '0000' '0000' '0000',
    'LCL'    : '0000' '0000' '0000' '0001',
    'ARG'    : '0000' '0000' '0000' '0010',
    'THIS'   : '0000' '0000' '0000' '0011',
    'THAT'   : '0000' '0000' '0000' '0100',
    'SCREEN' : '0100' '0000' '0000' '0000', # 16384,
    'KBD'    : '0110' '0000' '0000' '0000', # 24576,
    'R0'     : '0000' '0000' '0000' '0000',
    'R1'     : '0000' '0000' '0000' '0001',
    'R2'     : '0000' '0000' '0000' '0010',
    'R3'     : '0000' '0000' '0000' '0011',
    'R4'     : '0000' '0000' '0000' '0100',
    'R5'     : '0000' '0000' '0000' '0101',
    'R6'     : '0000' '0000' '0000' '0110',
    'R7'     : '0000' '0000' '0000' '0111',
    'R8'     : '0000' '0000' '0000' '1000',
    'R9'     : '0000' '0000' '0000' '1001',
    'R10'    : '0000' '0000' '0000' '1010',
    'R11'    : '0000' '0000' '0000' '1011',
    'R12'    : '0000' '0000' '0000' '1100',
    'R13'    : '0000' '0000' '0000' '1101',
    'R14'    : '0000' '0000' '0000' '1110',
    'R15'    : '0000' '0000' '0000' '1111',
    }

def parse_label(line):
    if line[-1] != ')':
        raise SyntaxError("Label declaration does not end with ')'")
    label = line[1:-1]
    try:
        float(label)
    except:
        return label
    else:
        raise ValueError("LABEL in (LABEL) declaration cannot be a number")


def compile_label(label, labels, program_counter):
    labels[label] = compile_address(program_counter)



###############################################################################
# C INSTRUCTIONS
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
#       j1 = 1 if jump when computation result is less than zero, otherwise 0
#       j2 = 1 if jump when computation result equals zero, otherwise 0
#       j3 = 1 if jump when computation result is greater than zero, otherwise 0

jumps = {
#   jump  : j1 j2 j3
    ''    : '000',
    'JLT' : '100',
    'JEQ' : '010',
    'JGT' : '001',
    'JLE' : '110',
    'JNE' : '101',
    'JGE' : '011',
    'JMP' : '111',
    }

# computation / a c1 c2 c3 c4 c5 c6:
#   addressing: a = 0 if A is selected for computation, 1 if M is selected for computation
#   operation: see dictionary below for available operations for A and D (when a=0)
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
    # PARSE
    # Check if too many = signs
    eq_split = line.split("=")
    if len(eq_split) > 2:
        raise SyntaxError("Only one '=' sign allowed in C-instruction")
    # Check if too many ; signs
    semicolon_split = line.split(";")
    if len(eq_split) > 2:
        raise SyntaxError("Only one ';' sign allowed in C-instruction")
    # Check if = comes before ;
    eq        = line.find("=") + 1
    semicolon = line.find(";") + 1
    if (eq > semicolon) and semicolon:
        raise SyntaxError("Assignment symbol '=' must come before jump delimiter ';' in C-instruction")
    # If neither = or ; are present warn the user that the instruction ultimately does nothing
    # print(eq, semicolon)
    if not( eq or semicolon ):
        import warnings
        warnings.warn("No '=' or ';' in C-instruction, this instruction will have no effect on register, memory or program counter", SyntaxWarning)
        destination, computation, jump = '', line, ''
    elif eq and not semicolon:
        destination, computation, jump = eq_split + ['']
    elif (not eq) and semicolon:
        destination, computation, jump = [''] + semicolon_split
    else:
        destination, computation, jump = [eq_split[0]] + eq_split[0].split(";")
    return destination, computation, jump

def compile_Cinstruction(destination, computation, jump):

    ###################################
    # DESTINATION
    ###################################

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

    # Warn user if there are extra character in the assignment
    if destination:
        import warnings
        warnings.warn("There are spurious characters in C-instruction assignment (left side of =)", SyntaxWarning)

    # final destination
    destination = A + D + M


    ###################################
    # JUMP
    ###################################
    try:
        jump = jumps[jump]
    except:
        print(jumps.key())
        raise SyntaxError('The jump instruction is not one of the options above')


    ###################################
    # ADDRESSING
    ###################################
    # A or M addressing
    A = bool(computation.find('A') + 1)
    M = bool(computation.find('M') + 1)
    if A and M:
        raise SyntaxError("A and M cannot be present at the same time in C-instruction, either A xor M must be selected")
    elif M:
        a = '1'
        # Now we can make A and M the same to simplify parsing of the computation
        computation = computation.replace('M','A')
        # Update A because now we transformed M to A even
        A = 1
    else:
        a = '0'

    ###################################
    # OPERATION
    ###################################
    # remember after parsing M we converted it to A, so we only need to check for computations with A and D
    try:
        computation = computations[computation]
    except:
        print(computations.keys())
        raise SyntaxError('Operation not recognized among the available computations listed above ')

    return '111' + a + computation + destination + jump + '\n'



###############################################################################
# COMPILATION FUNCTIONS
###############################################################################

# PASS 1 - LABEL PASS

def parse_labels(asm_filename, labels):
    # Reading labels pass
    with open(asm_filename, 'r') as assembly:
        program_counter = 0
        line_number = 1
        for line in assembly:
            line = clean_line(line)
            if not line:
                pass
            elif line[0] == '@':
                program_counter += 1
            elif line[0] == '(':
                try:
                    label = parse_label(line)
                    compile_label(label, labels, program_counter)
                except Exception as e:
                    raise Exception("Failed (LABEL) declaration in line " + str(line_number) + '\n') from e
            else:
                program_counter +=1
            line_number +=1

# PASS 2 - HACK MACHINE CODE PASS

def compile_hack_assembly(asm_filename, hack_filename, debug=False):
    if debug: print('Compiling file ' + asm_filename + ' into ' + hack_filename)
    with open(asm_filename, 'r') as assembly, open(hack_filename, 'w') as machine:
        program_counter = 0
        line_number = 1
        for line in assembly:
            line = clean_line(line)
            if debug: print("Compiling line " + str(line_number) + ": '" + line + "'")
            if not line:
                pass
            elif line[0] == '@':
                try:
                    instruction = parse_compile_Ainstruction(line, labels)
                    program_counter += 1
                    machine.write(instruction)
                    if debug: print(instruction)
                except Exception as e:
                    raise Exception("Failed A-instruction in line " + str(line_number) + '\n') from e
            elif line[0] == '(':
                pass
            else:
                try:
                    destination, computation, jump = parse_Cinstruction(line)
                    if debug: print("destination: ", destination,
                                  ", computation: ", computation,
                                  ", jump: ",  jump)
                    instruction = compile_Cinstruction(destination, computation, jump)
                    program_counter +=1
                    machine.write(instruction)
                    if debug: print(instruction)
                except Exception as e:
                    raise Exception("Failed C-instruction in line " + str(line_number) + '\n') from e
            line_number +=1



###############################################################################
# COMPILER
###############################################################################

# PARSE ARGUMENTS
import sys

# Check if input file is given
if len(sys.argv) == 1:
    print(  'please give a input file' +
            ' (will be treated as Hack assembly text file)',
            file=sys.stderr)

# Check if input file is text file
import mimetypes
if mimetypes.guess_type(sys.argv[1])[0] != 'text/plain':
    print(  'input file noplease give a input' +
            ' (will be treated as Hack assembly text file)',
            file=sys.stderr)

# Save input filename
asm_filename = sys.argv[1]


# OUTPUT FILE

# Create an output filename
if asm_filename.find(".asm") + 1:
    hack_filename = asm_filename.replace('.asm', '.hack')
else:
    hack_filename = asm_filename + '.hack'


# COMPILE

# Initialize the labels
labels = default_labels

# Do the labels pass (dictionaries are mutable and passed by reference)
parse_labels(asm_filename, labels)

# Do machine code pass
compile_hack_assembly(asm_filename, hack_filename, debug=True)




#def main():
#    print("Hello World!")
#
#if __name__ == "__main__":
#    compile_hack_asm()

