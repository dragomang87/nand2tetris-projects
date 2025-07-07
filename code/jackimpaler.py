###############################################################################
# JACK TOKENS AND COMMENTS
###############################################################################

###############################################################################
# JACK SYNTAX
###############################################################################

# AMBIGUOUS GRAMMAR

# There are many ambiguities
#   - Different terms for class, variable and function names are defined
#     but they all point to identifiers, so there is no way to distinguish them
#   - Symbols are defined, but used nowhere,
#     they are either part of the syntax or repeated as operators
#     (op or unaryOp)
#   - '-' is both op and unaryOp

'''
PROGRAM STRUCTURE

A Jack program is a collection of classes, each appearing in a separate
file, and each compiled separately. Each class is structured as follows:

class:              'class' className '{' classVarDec* subroutineDec* '}'
classVarDec:        ('static'|'field') type varName (',' varName)* ';'
type:               'int' | 'char' | 'boolean' | className
subroutineDec:      (‘constructor' | 'function'| 'method') (‘void'|type)
                    subroutineName '(' parameterList ')' subroutineBody
parameterList:      ((type varName) (',' type varName)*)?
subroutineBody:     '{' varDec* statements '}'
varDec:             'var' type varName (',' varName)* ';'
className:          identifier
subroutineName:     identifier
varName:            identifier



STATEMENTS

statements:         statement*
statement           : letStatement
                    | ifStatement
                    | whileStatement
                    | doStatement
                    | returnStatement
letStatement:       'let' varName ('[' expression ']')? '=' expression ';'
ifStatement:        'if'    '(' expression ')' '{' statements '}'
                    ('else'                    '{' statements '}' )?
whileStatement:     ‘while' '(' expression ')' '{' statements '}'
doStatement:        'do' subroutineCall  ';'
returnStatement:    'return' expression? ';'



EXPRESSIONS

expression:         term (op term)*
term                : integerConstant
                    | stringConstant
                    | keywordConstant
                    | varName
                    | varName '[* expression ']'
                    | subroutineCall
                    | '(' expression ')'
                    | unaryOp term
subroutineCall:     subroutineName '(' expressionList ')'
                    | ( className | varName)
                      '.' subroutineName '(' expressionList ')'
expressionList:     (expression (',' expression)* )?
op:                 '+' | '-' | '*' | '/' |
                    '&' | '|' |
                    '<' | '>' | '=' |
unaryOp:            '-' | '~' |
keywordConstant:    'true'|'false'|'null'|'this'



LEXICAL ELEMENTS (TOKENS)

keyword:            'class'|'constructor'|'function'|'method'|'field'|
                    'let'|'do' |'if'|'else'|'while'|'return'|
                    'var'|'int'|'char'|'boolean'|'void'|'static'|
                    'true'|'false'|'null'|'this'|
keyword             : 'class'| 'int' | 'char' | 'boolean' | 'constructor' |
                    | 'true' | 'var' | 'void' | 'method'  |
                    | 'false'| 'let' | 'while'| 'return'  |
                    | 'null' | 'if'  | 'else' | 'function'|
                    | 'this' | 'do'  | 'field'| 'static'  |
symbol:             | '{' | '}' | '.' | ',' | ';' |
                    | '(' | ')' | '+' | '-' | '*' | '/' |
                    | '[' | ']' | '&' | '|' | '~' | '<' | '>' | '=' |
integerConstant:    decimal in 0 ... 32767
StringConstant:     '"' characters without quote or newline '"'
identifier:         letters, digits, and _ not starting with a digit.
'''

'''
PROGRAM STRUCTURE

A Jack program is a collection of classes, each appearing in a separate
file, and each compiled separately. Each class is structured as follows:

class:              'class' identifier '{'
                        classVarDec*
                        subroutineDec*
                        '}'
subroutineDec:      (‘constructor' | 'function'| 'method')
                    (‘void'|type) identifier parameters codeblock(True)
{subroutineBody}:   codeblock(True)
[parameterDef]:     '(' parameterList ')'
{parameterList}:    (type identifier ',')* (type identifier)?

classVarDec:        ('static'|'field') variables
varDec:             'var'              variables
[variables]:        type identifier (',' identifier)* ';'
[type]:             'int' | 'char' | 'boolean' | identifier



STATEMENTS

[codeblock(body)]:  '{'
                        varDec* if body=True
                        statements
                    '}'
{statements}:       ( letStatement
                    | ifStatement
                    | whileStatement
                    | doStatement
                    | returnStatement
                    )*
letStatement:       'let' identifier ('[' expression(']') )?
                      '=' expression(';')
ifStatement:        'if'    '(' expression(')') code_block(False)
                    ('else'                     code_block(False) )?
whileStatement:     ‘while' '(' expression(')') code_block(False)
doStatement:        'do' identifier ('.' identifier)? '(' expressionList ';'
returnStatement:    'return' (';'|expression(';'))



EXPRESSIONS

expression(end):    term (op term)* end
term                : integerConstant
                    | stringConstant
                    | 'true'|'false'|'null'|'this'
                    | identifier ('[' expression(']') )?
                    | identifier ('.' identifier)? '(' expressionList
                    | ('-' | '~')? term
                    | '(' expression(')')
expressionList:     (expression (',' expression)* )? ')'
(op):               '+' | '-' | '*' | '/' |
                    '&' | '|' |
                    '<' | '>' | '=' |



LEXICAL ELEMENTS (TOKENS)

integerConstant
stringConstant
identifier
'''

from jackalyzer import Syntacker

###############################################################################
# JACK COMPILER
###############################################################################




###############################################################################
# JACK COMPILER SCRIPT
###############################################################################

if __name__ == "__main__":
    # INPUT FILE
    import sys
    # Check if input file is given
    if len(sys.argv) == 1:
        print(
            "no input file provided\n"
            "please give a text input file "
            "(it will be treated as Hack Virtual Machine text file)",
            file=sys.stderr
            )
        sys.exit(1)

    # DISTINGUISH CALL NAME
    # The submission asks to produce .xml files but also provides .xml files
    # By default the tockenizer and analyzer do not use .xml extension
    # unless the analyzer is called with the submission name (JackAnalyzer.py)
    # instead of the original filename jackalizer.py
    submission = True if sys.argv[0] == "JackCompiler.py" else False
    print("Compiling for submission: ", submission)
    arguments = sys.argv[1:]

    import os

    # GET INPUT FILES
    jack_files     = [arg for arg in arguments if os.path.isfile(arg)]
    print("files:", jack_files)

    # GET INPUT FOLDERS
    jack_folders   = [arg for arg in arguments if os.path.isdir (arg)]
    # Remove trailing / from folders, otherwise .basename() returns ""
    clean_folder = lambda folder: folder[:-1] if folder[-1] == "/" else folder
    jack_folders   = [clean_folder(folder) for folder in jack_folders]
    print("folders:", jack_folders)

    # COMPILE INPUT FILES
    for jack_file in jack_files:
        print(f"Tockenizing and analyzing Jack file {jack_file}")
        jack = Syntacker(jack_file, analyze=True)
        print(jack.syntack)

    # COMPILE INPUT FOLDERS
    for folder in jack_folders:
        # Find all .jack files in folder
        import glob
        jack_files = glob.glob(f"{folder}/*.jack")
        # Analyze all files
        # (the compiler function returns the output filename)
        for jack_file in jack_files:
            print(f"Tockenizing and analyzing Jack file {jack_file}")
            syntack = Syntacker(jack_file, analyze=True).syntack
