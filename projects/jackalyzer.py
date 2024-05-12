################################################################################
# JACK TOKENS AND COMMENTS
################################################################################

# Tokens vs Syntax:
#   - tokens are always the same
#     e.g. ) and ( are (or at least should be) always two independent tokens,
#     in this case symbol tokens as defined below
#   - syntax depend on context from previous syntax
#     e.g. parenthesis can be either expression or arguments

# Notes:
#   - tokens come before syntax
#   - strings and comments are part of syntax but are parsed at tokens
#     thus strings and comments behave somewhere in between tokens and syntax;
#     this is unavoidable because while inside strings and comments
#       - spaces are part of the string/comment and not tokens separators
#       - tokens are not tokens anymore
#       - strings and comments inside each other are not strings or comment
#   - pure tokenizing would mark ", //, /*, */  and spaces all as token,
#     instead syntax matching opening and closing strings and comments
#   - comments and strings can disable each other and other tokens
#       - // or /* inside a string are not comments and
#       - "  inside a comment is not a string
#       - tokens inside comments or strings are not tokens
#       - block comments spill over to other lines
#   - comments and strings are part of the syntax
#     but are thus parsed the token stage

# There are two types of comments
#   - inline comments: everything between // and end of line
#     (when not inside a string or block comment)
#   - block comments: everything between /* and */ including newlines
#     (when not inside string or inline comment)
#     because opening and closing delimiter are different
#     this raises the question of whether block comments
#       - nest each other
#       - disable each other

# True tokenization:
#   - everything, including spaces " // /* and */ are tokens
#   - syntax parsing and abstract tree would then
#     reconstruct the strings and remove comments on the next pass

# There are five types of tokens (tags):
tags = ['keyword', 'symbol', 'intConst', 'stringConst', 'identifier'],

# Integer (intConst)
#   digits

# Identifiers:
#   letters, digits and underscores not starting with a digit

# Strings (stringConst)
#   any characters except " and newlines enclosed by "

# Keywords and Symbols:
TAGS =  {
        'keyword':
                ['class'
                ,'constructor'
                ,'function'
                ,'method'
                ,'field'
                ,'static'
                ,'var'
                ,'int'
                ,'char'
                ,'boolean'
                ,'void'
                ,'true'
                ,'false'
                ,'null'
                ,'this'
                ,'let'
                ,'do'
                ,'if'
                ,'else'
                ,'while'
                ,'return'
                ],
        'symbol': [
            '{', '}', '(', ')', '[', ']',
            '.', ',', ';',
            '+', '-', '*', '/',
            '&', '|', '~', '<', '>', '=',
            ],
        }

################################################################################
# JACK SYNTAX
################################################################################

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
ifStatement:        'if''(' expression ')' '{' statements '}
                    ('else'                '{' statements '} )?
whileStatement:     ‘while''(' expression ')' '{' statements '}'
doStatement:        'do' subroutineCall ';'
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
subroutineCall:     subroutineName '(' expressionList )'
                    | ( className | varName)
                      '.' subroutineName '(' expressionList ')'
expressionList:     (expression (', expression)* )?
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

# UNAMBIGUOUS GRAMMAR

# Most ambiguities have been removed
#   - only identifiers instead of names
#   - removed unaryOp and merged into the syntax
#   - no symbols, only syntax and operator symbols
#     does not change the fact that '-' has two roles
#     (like '=' and parentheses)
#   - merged subroutineBody into subroutine declaration
#     since it is the only place where it was used
#   - removed 'statement' since the rest only ever calls 'statements'
#   - simplified subroutine call, facilitated by the identifier merge,
#     and merged into term, since function calls and array indexing
#     must cooperate to figure out which one is the correct one
#   - StringConstant is actually stringConstant,
#     the grammar from the slides has a typo
# However, not all these symplifications can be kept
# because rules imply XML tags, so we still need to produce
# the tags for:
#   - subroutineBody
#   - syntax symbols, they keep the tokenizer tag
# but not
#   - op and unaryOp
#     they do not appear in the comparison files
#     the generic 'symbol' tag is kept
#   - keywordConstant
#     they do not appear in the comparison files
#     the generic 'keyword' tag is kept
#   - subroutineCall
#     It is suggested by the course to handle subroutineCall within term,
#     and the tag is not present in any of the comparison files,
#     so term does not need to take care of adding the subroutineCall tag

'''
PROGRAM STRUCTURE

A Jack program is a collection of classes, each appearing in a separate
file, and each compiled separately. Each class is structured as follows:

class:              'class' identifier '{'
                        classVarDec*
                        subroutineDec*
                        '}'
classVarDec:        ('static'|'field') type identifier (',' identifier)* ';'
type:               'int' | 'char' | 'boolean' | identifier
subroutineDec:      (‘constructor' | 'function'| 'method') (‘void'|type)
                    identifier '(' parameterList ')' '{'
                        varDec*
                        statements
                        '}'
parameterList:      ((type identifier) (',' type identifier)*)?
varDec:             'var' type identifier (',' identifier)* ';'



STATEMENTS

statements:         ( letStatement
                    | ifStatement
                    | whileStatement
                    | doStatement
                    | returnStatement
                    )*
letStatement:       'let' identifier ('[' expression ']')? '=' expression ';'
ifStatement:        'if''(' expression ')' '{' statements '}
                    ('else'                '{' statements '} )?
whileStatement:     ‘while''(' expression ')' '{' statements '}'
doStatement:        'do' subroutineCall ';'
returnStatement:    'return' expression? ';'



EXPRESSIONS

expression:         term (op term)*
term                : integerConstant
                    | stringConstant
                    | keywordConstant
                    | identifier ('[* expression ']')?
                    | identifier ('.' identifier)? '(' expressionList ')'
                    | ('-' | '~')? term
                    | '(' expression ')'
expressionList:     (expression (', expression)* )?
op:                 '+' | '-' | '*' | '/' |
                    '&' | '|' |
                    '<' | '>' | '=' |
keywordConstant:    'true'|'false'|'null'|'this'



LEXICAL ELEMENTS (TOKENS)

keyword             : 'class'| 'int' | 'char' | 'boolean' | 'constructor' |
                    | 'true' | 'var' | 'void' | 'method'  |
                    | 'false'| 'let' | 'while'| 'return'  |
                    | 'null' | 'if'  | 'else' | 'function'|
                    | 'this' | 'do'  | 'field'| 'static'  |
integerConstant:    decimal in 0 ... 32767
stringConstant:     '"' characters without quote or newline '"'
identifier:         letters, digits, and _ not starting with a digit.
'''


################################################################################
# JACK XML SYNTAX
################################################################################

# - some symbols must be translated:
#
# - quotes are removed from strings


################################################################################
# JACK SYNTAX ANALYZER
################################################################################


class Syntacker():

    def __init__(self, jack_filename, analyze=False, strict=True):
        from tackenizer import tokenize
        self.tackens = tokenize(jack_filename, output_file=False)
        self.index   = -1
        if analyze:
            self.syntack = self.analyze(self.tackens)

    def analyze(self):
        self.index   = -1
        self.syntack = self.syntack_class(self.tackens)
        if self.index != len(self.tackens):
            if strict:
                raise SyntaxError(
                        f"Class terminated but more tokens found: "
                        f"{self.tackens[self.index:]}"
                        )
            else:
                from warnings import warn
                warn(   f"Class terminated but more tokens found: "
                        f"{self.tackens[self.index:]}"
                        )

    def next(self):
        self.index += 1
        return self.tackens[self.index]

    def back(self, n=1):
        self.index -= n
        return


    #PROGRAM STRUCTURE

    #class:             'class' identifier '{'
    #                       classVarDec*
    #                       subroutineDec*
    #                       '}'
    #classVarDec:       ('static'|'field') type identifier (',' identifier)* ';'
    #type:              'int' | 'char' | 'boolean' | identifier
    #subroutineDec:     (‘constructor' | 'function'| 'method') (‘void'|type)
    #                   identifier '(' parameterList ')' '{'
    #                       varDec*
    #                       statements
    #                       '}'
    #parameterList:     ((type identifier) (',' type identifier)*)?
    #varDec:            'var' type identifier (',' identifier)* ';'

    # Actually used tags:
    #   - class
    #   - classVarDec
    #   - subroutineDec
    #   - varDec
    #
    # Always used tags even if empty:
    #   - parameterList
    #
    # Unused tags:
    #   - type

    def parse_class(self):
        #class:         'class' identifier '{'
        #                   classVarDec*
        #                   subroutineDec*
        #                   '}'
        jack_class = ()
        try:
            # Parse 'class' keyword
            token = self.next()
            if token[1] == 'class':
                jack_class += ('class', token)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"Jack files must start with a 'class' definition"
                        )
            # Parse identifier
            token = self.next()
            if token[0] == 'identifier':
                jack_class += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"'class' not followed by an identifier "
                        f"(the class name)"
                        )
            # Parse opening bracket
            token = self.next()
            if token[1] == '{':
                jack_class += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"class identifier not followed by { "
                        f"(the opening of the class body)"
                        )
            # Parse variable declarations
            jack_class += self.parse_classVarDec()
            # Parse methods and function declarations
            jack_class += self.parse_subroutineDec()
            # Parse closing bracket
            token = self.next()
            if token[1] == '}':
                jack_class += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"class body not closed by } "
                        f"in class declaration {jack_class}"
                        )
        except IndexError:
            raise SyntaxError(
                    f"Run out of tokens parsing 'class'"
                    )

        return jack_class

    def parse_classVarDec(self):
        #classVarDec:   ('static'|'field') type identifier (',' identifier)* ';'
        jack_class_variables = ()
        while True:
            # Check if there is a variable declaration
            # If not then just exit the loop
            # no error can come from this
            token = self.next()
            if token[1] not in ['static', 'field']:
                self.back()
                break
            # If variable declaration then start parsing
            jack_class_variable = ('classVarDec', token)
            # Parse type
            token = self.next()
            if token[1] in ['int', 'char', 'boolean'] \
            or token[0] == 'identifier':
                jack_class_variable += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"'static' and 'field' not followed by "
                        f"'int', 'char', 'boolean' or identifier "
                        f"(the variables type) "
                        f"in class variable declaration "
                        f"{jack_class_variable}"
                        )
            # Parse first variable name
            token = self.next()
            if token[0] == 'identifier':
                jack_class_variable += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"'int', 'char', 'boolean' or identifier "
                        f"not followed by an identifier "
                        f"(the name of the variable) "
                        f"in class variable declaration "
                        f"{jack_class_variable}"
                        )
            # Parse additional variables
            token = self.next()
            while token[1] == ',':
                jack_class_variable += (token,)
                token = self.next()
                if token[0] == 'identifier':
                    jack_class_variable += (token,)
                    token = self.next()
                else:
                    raise SyntaxError(
                            f"FAIL parsing token {token}: "
                            f"comma not followed by identifier "
                            f"(the name of the next variable) "
                            f"in class variable declaration "
                            f"{jack_class_variable}"
                            )
            # Parse closing semicolon
            if token[1] == ';':
                jack_class_variable += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"name identifiers should be followed by commas or ;"
                        f"in class variable declaration "
                        f"{jack_class_variable}"
                        )
            # Add the variable declaration to the list
            jack_class_variables += (jack_class_variable,)

    def parse_subroutineDec(self):
        #subroutineDec: (‘constructor' | 'function'| 'method') (‘void'|type)
        #               identifier '(' parameterList ')' '{'
        #                   varDec*
        #                   statements
        #                   '}'
        jack_class_subroutine = ()
        while True:
            # Check if there is a subroutine declaration
            # If not then just exit the loop
            # no error can come from this
            token = self.next()
            if token[1] not in ['constructor', 'function', 'method']:
                self.back()
                break
            # If subroutine declaration then start parsing
            jack_class_subroutine = ('subroutineDec', token)
            # Parse type
            token = self.next()
            if token[1] in ['void', 'int', 'char', 'boolean'] \
            or token[0] == 'identifier':
                jack_class_subroutine += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"'constructor', 'method' and 'function' not followed by "
                        f"'void', 'int', 'char', 'boolean' or identifier "
                        f"(the return type of the subroutine) "
                        f"in subroutine declaration "
                        f"{jack_class_subroutine}"
                        )
            # Parse subroutine name
            token = self.next()
            if token[0] == 'identifier':
                jack_class_subroutine += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"subroutine return type "
                        f"'void', 'int', 'char', 'boolean' or identifier "
                        f"not followed by an identifier "
                        f"(the name of the subroutine) "
                        f"in subroutine declaration"
                        f"{jack_class_subroutine}"
                        )
            # Parse opening (
            token = self.next()
            if token[1] == '(':
                jack_class_subroutine += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"subroutine name identifier not followed by ( "
                        f"(opening of the subroutine parameters) "
                        f"in subroutine declaration"
                        f"{jack_class_subroutine}"
                        )
            # Parse parameter list
            jack_class_subroutine += self.parse_parameterList()
            # Parse closing )
            token = self.next()
            if token[1] == ')':
                jack_class_subroutines += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"subroutine parameters not closed by ) "
                        f"in subroutine declaration"
                        f"{jack_class_subroutine}"
                        )
            # Parse subroutineBody
            jack_class_subroutine += self.parse_subroutineBody()
            # Add the subroutine declaration to the list
            jack_class_subroutines += (jack_class_subroutine,)

    def parse_parameterList(self):
    def parse_subroutineBody(self):






    #type:               'int' | 'char' | 'boolean' | identifier
    #subroutineDec:      (‘constructor' | 'function'| 'method') (‘void'|type)
    #                    identifier '(' parameterList ')' '{'
    #                        varDec*
    #                        statements
    #                        '}'
    #parameterList:      ((type identifier) (',' type identifier)*)?
    #varDec:             'var' type identifier (',' identifier)* ';'


    #STATEMENTS
    #
    #statements:         ( letStatement
    #                    | ifStatement
    #                    | whileStatement
    #                    | doStatement
    #                    | returnStatement
    #                    )*
    #letStatement:       'let' identifier ('[' expression ']')? '=' expression ';'
    #ifStatement:        'if''(' expression ')' '{' statements '}
    #                    ('else'                '{' statements '} )?
    #whileStatement:     ‘while''(' expression ')' '{' statements '}'
    #doStatement:        'do' subroutineCall ';'
    #returnStatement:    'return' expression? ';'



    #EXPRESSIONS
    #
    #expression:         term (op term)*
    #term                : integerConstant
    #                    | stringConstant
    #                    | keywordConstant
    #                    | identifier ('[* expression ']')?
    #                    | subroutineCall
    #                    | ('-' | '~')? term
    #                    | '(' expression ')'
    #subroutineCall:     identifier ('.' identifier)? '(' expressionList ')'
    #expressionList:     (expression (', expression)* )?
    #op:                 '+' | '-' | '*' | '/' |
    #                    '&' | '|' |
    #                    '<' | '>' | '=' |
    #keywordConstant:    'true'|'false'|'null'|'this'



    #LEXICAL ELEMENTS (TOKENS)
    #
    #keyword             : 'class'| 'int' | 'char' | 'boolean' | 'constructor' |
    #                    | 'true' | 'var' | 'void' | 'method'  |
    #                    | 'false'| 'let' | 'while'| 'return'  |
    #                    | 'null' | 'if'  | 'else' | 'function'|
    #                    | 'this' | 'do'  | 'field'| 'static'  |
    #integerConstant:    decimal in 0 ... 32767
    #StringConstant:     '"' characters without quote or newline '"'
    #identifier:         letters, digits, and _ not starting with a digit.




################################################################################
# JACK TOKENIZER SCRIPT
################################################################################

if __name__ == "__main__":
    # INPUT FILE
    import sys
    # Check if input file is given
    if len(sys.argv) == 1:
        print(
            f"no input file provided\n"
            f"please give a text input file "
            f"(it will be treated as Hack Virtual Machine text file)",
            file=sys.stderr
            )
        sys.exit(1)

    # COMPILE input file
    tokenize(sys.argv[1], debug=False)
