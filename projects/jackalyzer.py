###############################################################################
# JACK TOKENS AND COMMENTS
###############################################################################

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
TAGS = {
        'keyword': [
            'class',
            'constructor',
            'function',
            'method',
            'field',
            'static',
            'var',
            'int',
            'char',
            'boolean',
            'void',
            'true',
            'false',
            'null',
            'this',
            'let',
            'do',
            'if',
            'else',
            'while',
            'return',
            ],
        'symbol': [
            '{', '}', '(', ')', '[', ']',
            '.', ',', ';',
            '+', '-', '*', '/',
            '&', '|', '~', '<', '>', '=',
            ],
        }

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

# IGNORED TAGS

# Some tags are not actually used in the Jack syntax analyzer
# as shown by the lack of output in
#     STRUCTURE="Name\|type\|statement>"
#     EXPRESSIONS="unaryOp\|op\|keywordConstant\|subroutineCall"
#     grep "$STRUCTURE\|$EXPRESSIONS" 10/*/*.xml
# The following have been explicitly mentioned in module II.4.7:
#   - *Name: varName, className, subroutineName
#   - type
#   - statement
#   - subroutineCall
# The following were not mentioned
#   - op
#   - unaryOp
#   - keywordConstant
# Instead these syntax tags are handled as follows
#   - ignored, identifier is kept
#   - ignored, keyword and identifier are kept
#   - ignored, the list of syntax tokens is kept
#              as part of the term syntax or doStatement syntax
#   - ignored, symbol is kept
#   - ignored, symbol is kept
#   - ignored, keyword is kept

# Some of the ignored tags are due to grammar issues
# while other are just because of simplification.
# In particular, the following are just for simplification:
#   - type
#   - statement
#   - subroutineCall
#   - op
#   - unaryOp
#   - keywordConstant
# While the following is because they make the grammar ambigous:
#   - *Name: varName, className, subroutineName
# Since all of these are identifiers,
# there is no way to distinguish them unless
# we anticipate the role of the compiler
# and keep track of variable, class and subroutine declarations
# and match names to these three classes.
#


# UNAMBIGUOUS GRAMMAR AND MODIFICATIONS

# There is a difference between ignoring a tag
# and not actually needing the grammar rule
# as a separatedly-implemented parsing function:
#   - some ignored tags make the grammar simpler are
#       -- *Name
#       -- statement
#       -- op
#       -- unaryOp
#       -- keywordConstant
#   - some ignored tags that is still better to implement are
#       -- type
#       -- subroutineCall
#   - some grammars that are better implemented
#     including some of the parent grammar are
#       -- parameterList
#       -- expressionList
#
# We therefore modify the grammar to reflect exactly
# how it is implemented in this module.
# To this end, we introduce some additional grammar notation:
#   - <rule>: ...
#     is for a rule that is both implemented as a function and tagged
#   - [rule]: ...
#     is for a rule that is implemented as function but not tagged
#   - {rule}: ...
#     is for a rule that is not implemented as function but is tagged,
#     the implementation is thus merged in the parent-rule implementation
#   - (rule): ...
#     is for a rule that is neither implemented as a function nor tagged
#
# The final rule differences include:
#   - Only identifiers instead of names
#   - Removed unaryOp and merged into the syntax
#   - 'op' rule becomes '(op)' rule,
#     does not change the fact that '-' has two roles
#     (like '=' and parentheses)
#   - Removed 'statement' and merged into 'statements'
#     since the rest only ever calls 'statements'
#   - Created '[variables]' rule shared by 'classVarDec' and 'varDec'
#   - Simplified 'subroutineCall', facilitated by the identifier merge,
#     and merged into term, since function calls and array indexing
#     must cooperate to figure out which one is the correct one;
#     This merging is actually explicitly suggested by the course.
#   - StringConstant is actually stringConstant,
#     the grammar from the slides has a typo
#   - We allow trailing comma in 'parameterDef' and 'parameterPass',
#     this simlifies the grammar
# There are also some rule changes that stem from the same concept.
# Whenever there is a list to parse that could be empty,
# the parser thus needs to look at tokens until it finds a token
# that does not go in the list.
# It the parser function stops there then it has to backtrack one token,
# so that the next function can use this last token unsused by the list parser.
# However, lists always need some kind of termnination,
# so if the list parser is allowed to parse it's own terminator
# then it will stop at the terminator and not further,
# thus avoiding the need to back track.
# Therefore the following changes have been made
#   - Created '[parameterDef]'  merging the parentheses in 'parameterList'
#     which now becomes '{parameterList}'
#   - Created '[parameterPass]' merging the parentheses in 'expressionList'
#     which now becomes '{expressionList}'
#   - Created '[codeblock(body)]' with body = True, False
#     merging the curly brackets in subroutineBody and statements
#     if body = True, then the parser will check for varDec first
#   - Gave expression an argument for the terminal element
#


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
doStatement:        'do' identifier ('.' identifier)? parameterPass ';'
returnStatement:    'return' (';'|expression(';'))



EXPRESSIONS

expression(end):    term (op term)* end
term                : integerConstant
                    | stringConstant
                    | 'true'|'false'|'null'|'this'
                    | identifier ('[' expression(']') )?
                    | identifier ('.' identifier)? parameterPass
                    | ('-' | '~')? term
                    | '(' expression(')')
[parameterPass]:    '(' expressionList ')'
{expressionList}:   (expression ',')* expression?
(op):               '+' | '-' | '*' | '/' |
                    '&' | '|' |
                    '<' | '>' | '=' |



LEXICAL ELEMENTS (TOKENS)

integerConstant
stringConstant
identifier
'''


###############################################################################
# JACK XML SYNTAX
###############################################################################

# - some symbols must be translated:
#
# - quotes are removed from strings


###############################################################################
# JACK SYNTAX ANALYZER
###############################################################################


def is_jack_type(self, token, void=False):
    # [type]:       'int' | 'char' | 'boolean' | identifier
    types = ['int', 'char', 'boolean']
    if void:
        types += ['void']
    return token[1] in types or token[0] == 'identifier'


def tree_to_xml(tree):
    tag = tree[0]
    xml = [f"<{tag}>"]
    from tackenizer import tags
    if tag in tags:
        xml += [tree[1]]
    else:
        xml += ["\n"] + [tree_to_xml(branch) for branch in tree[1:]]
    xml = "".join(xml + [f"</{tag}>\n"])


class Syntacker():

    def __init__(self,
                 jack_filename,
                 analyze = False,
                 xml     = False,
                 save    = False,
                 strict  = True,
                 ):
        # Store file basename
        from tackenizer import remove_jack_extension
        self.jack_name = remove_jack_extension(jack_filename)
        # Tokenize first
        from tackenizer import tokenize
        self.tackens = tokenize(jack_filename, output_file=False)
        # Position the analyzer at the beginning
        self.index = -1
        # Initialize the statement parser dictionary
        self.STATEMENTS = {
                'let'   : self.parse_let    ,
                'if'    : self.parse_if     ,
                'while' : self.parse_while  ,
                'do'    : self.parse_do     ,
                'return': self.parse_return ,
                }
        # Initialize the syntax tree and xml variables
        self.syntack = None
        self.jaxml   = None
        # Analyze if requested
        if analyze:
            self.syntack = self.analyze(self.tackens)
        # Produce xml if requested
        if xml:
            self.make_xml()
        # Save to output file if requested
        if save:
            self.save_xml()

    def analyze(self, strict=True):
        # Reset to beginning
        self.index = -1
        # Parse one class as expected per file
        self.syntack = self.syntack_class(self.tackens)
        # Check if there is dead code after the class
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

    def make_xml(self):
        if self.syntack is None:
            self.analyze()
        self.jaxml = tree_to_xml(self.syntack)

    def save_xml(self):
        if self.jaxml is None:
            self.make_xml()
        with open(self.jack_name + ".jaxml", 'w') as xml:
            xml.write(self.jaxml)

    def next(self):
        self.index += 1
        return self.tackens[self.index]

    def back(self, n=1):
        self.index -= n
        return

    ###########################################################################
    # PROGRAM STRUCTURE
    ###########################################################################

    # class:            'class' identifier '{'
    #                       classVarDec*
    #                       subroutineDec*
    #                       '}'
    # classVarDec:      ('static'|'field') variables
    # subroutineDec:    (‘constructor' | 'function'| 'method') (‘void'|type)
    #                   identifier '(' parameterList ')' subroutineBody
    # parameterList:    (type identifier ',')* (type identifier)?
    # varDec:           'var' variables
    # variables:        type identifier (',' identifier)* ';'
    # (type):             'int' | 'char' | 'boolean' | identifier

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
        # class:        'class' identifier '{'
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
                        f"class identifier not followed by ""{ "
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
                        f"class body not closed by ""} "
                        f"in class declaration {jack_class}"
                        )
        except IndexError:
            raise SyntaxError(
                    f"Run out of tokens parsing 'class' {jack_class}"
                    )

        return jack_class

    def parse_classVarDecs(self):
        # classVarDec: ('static'|'field') type identifier (',' identifier)* ';'
        jack_class_variables = ()
        while True:
            # Check if there is a variable declaration
            # If not then just exit the loop
            # no error can come from this
            token = self.next()
            if token[1] not in ['static', 'field']:
                self.back()
                break
            # If variable declaration then parse variables
            jack_class_variable   = ('classVarDec', token)
            # Use helper function shared with subroutine variable declaration
            jack_class_variable  += self.parse_variable_list()
            # Add the variable declaration to the list
            jack_class_variables += (jack_class_variable,)

    ###########################################################################

    def parse_subroutineDecs(self):
        # subroutineDec: (‘constructor' | 'function'| 'method')
        #                (‘void'|type) identifier parameters codeblock[True]
        # (type):        'int' | 'char' | 'boolean' | identifier
        jack_class_subroutines = ()
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
            if is_jack_type(token, void=True):
                jack_class_subroutine += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"'constructor', 'method' and 'function' not followed "
                        f"by 'void', 'int', 'char', 'boolean' or identifier "
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
            # Parse parameter list with parenthesis
            jack_class_subroutine  += self.parse_parameterDef()
            # Parse subroutineBody
            jack_class_subroutine  += (self.parse_codeblock(body=True),)
            # Add the subroutine declaration to the list
            jack_class_subroutines += (jack_class_subroutine,)
        return jack_class_subroutines

    def parse_parameterDef(self):
        # parameters:   '(' parameterList ')'
        # parameterList:(type identifier ',')* (type identifier)?
        # (type):       'int' | 'char' | 'boolean' | identifier
        jack_parameters = ()
        # Parse opening (
        token = self.next()
        if token[1] == '(':
            jack_parameters += (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"subroutine name identifier not followed by ( "
                    f"(opening of the subroutine parameters) "
                    f"in subroutine declaration"
                    )
        # Parse parameter list
        jack_list = ('parameterList',)
        while True:
            # Check for parameter type
            # if not present then exit
            token = self.next()
            if is_jack_type(token):
                jack_list += (token,)
            else:
                break
            # If type was found expect an identifier
            token = self.next()
            if token[0] == 'identifier':
                jack_list += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"'int', 'char', 'boolean' or identifier "
                        f"(the parameter type)"
                        f"not followed by identifier"
                        f"(the parameter name) "
                        f"in subroutine parameter list "
                        f"{jack_parameters}"
                        )
            # Exit if the next token is not a comma
            token = self.next()
            if token[1] == ',':
                jack_list += (token,)
            else:
                break
        # Join parameterList and the parenthesis
        jack_parameters += (jack_list,)
        # We come out of the while loop with one unparsed token
        # Parse closing )
        if token[1] == ')':
            jack_parameters += (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"subroutine parameters not closed by ) "
                    f"in subroutine declaration"
                    f"{jack_parameters}"
                    )

    def parse_varDecs(self):
        # varDec:       'var' type identifier (',' identifier)* ';'
        jack_class_variables = ()
        while True:
            # Check if there is a variable declaration
            # If not then just exit the loop
            # no error can come from this
            token = self.next()
            if token[1] != 'var':
                self.back()
                break
            # If variable declaration then parse variables
            jack_class_variable   = ('varDec', token)
            # Use helper function shared with class variable declaration
            jack_class_variable  += self.parse_variable_list()
            # Add the variable declaration to the list
            jack_class_variables += (jack_class_variable,)

    def parse_variable_list(self, declaration):
        # Helper parser for classVarDec and varDec:
        #   type identifier (',' identifier)* ';'
        declaration = ()
        # Parse type
        token = self.next()
        if is_jack_type(token):
            declaration += (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"'static', 'field' or 'var' not followed by "
                    f"'int', 'char', 'boolean' or identifier "
                    f"(the variables type) "
                    f"in class or subroutine variable declaration "
                    f"{declaration}"
                    )
        # Parse first variable name
        token = self.next()
        if token[0] == 'identifier':
            declaration += (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"variable type "
                    f"('int', 'char', 'boolean' or identifier) "
                    f"not followed by an identifier "
                    f"(the name of the variable) "
                    f"in class or subroutine variable declaration "
                    f"{declaration}"
                    )
        # Parse additional variables
        token = self.next()
        while token[1] == ',':
            declaration += (token,)
            token = self.next()
            if token[0] == 'identifier':
                declaration += (token,)
                token = self.next()
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"comma not followed by identifier "
                        f"(the name of the next variable) "
                        f"in class or subroutine variable declaration "
                        f"{declaration}"
                        )
        # Parse closing semicolon
        if token[1] == ';':
            declaration += (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"name identifiers should be followed by commas or ;"
                    f"in class or subroutine variable declaration "
                    f"{declaration}"
                    )
        return declaration

    ###########################################################################
    # STATEMENTS
    ###########################################################################
    #
    # {subroutineBody}: codeblock(True)
    # [codeblock(body)]:'{'
    #                       varDec* if body=True
    #                       statements
    #                   '}'
    # {statements}:      ( letStatement
    #                    | ifStatement
    #                    | whileStatement
    #                    | doStatement
    #                    | returnStatement
    #                    )*
    # letStatement:     'let' identifier ('[' expression ']')?
    #                     '=' expression ';'
    # ifStatement:      'if'    '(' expression ')' codeblock[False]
    #                   ('else'                    codeblock[False] )?
    # whileStatement:   ‘while' '(' expression ')' codeblock[False]
    # doStatement:      'do' identifier ('.' identifier)? '(' parameterPass ';'
    # returnStatement:  'return' expression? ';'
    #

    def parse_codeblock(self, body=False):
        # {subroutineBody}:
        #                codeblock(True)
        # [codeblock(body)]:
        #                '{'
        #                    varDec* if body=True
        #                         statements
        #                '}'
        # {statements}:  ( letStatement
        #                | ifStatement
        #                | whileStatement
        #                | doStatement
        #                | returnStatement
        #                )*
        # Parse opening bracket
        token = self.next()
        if token[1] == '{':
            jack_codeblock = (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"expected code block starting with ""{ "
                    f"(the opening of subroutine, if, else or while body)"
                    )
        # Parse variable declarations if in a subroutine Body
        if body:
            jack_codeblock += self.parse_varDecs()
        # Parse statements
        jack_statements = ('statements',)
        while True:
            token = self.next()
            if token[1] in self.STATEMENT:
                jack_statement   = (token[1] + 'Statement', token)
                jack_statement  += self.STATEMENT[token[1]]()
                jack_statements += (jack_statement,)
            else:
                break
        # Parse closing bracket
        if token[1] == '}':
            jack_codeblock += (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"statements not closed by ""} "
                    f"in {jack_codeblock}"
                    )
        # If subroutineBody then add the tag
        if body:
            return ('subroutineBody', jack_codeblock)
        else:
            return jack_codeblock

    def parse_let(self):
        # letStatement: 'let' identifier ('[' expression ']')?
        #                 '=' expression ';'
        # Parse identifier
        token = self.next()
        if token[0] != 'identifier':
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"'let' not followed by identifier"
                    f"(the name of the variable or array) "
                    f"in let statement"
                    )
        statement = (token,)
        # Parse array
        token = self.next()
        if token[1] == '[':
            statement += (token,) + self.parse_expression(end=']')
            # Ensure we still have a token to parse if [ was eaten
            token = self.next()
        # Parse assignment
        if token[1] != '=':
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"variable or array not followed by ="
                    f"(assignment symbol) "
                    f"in let statement"
                    )
        return statement + (token,) + self.parse_expression(end=';')

    def parse_if(self):
        # ifStatement:  'if'    '(' expression ')' codeblock
        #               ('else'                    codeblock )?
        token = self.next()
        if token[1] == '(':
            statement = (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"if not followed by ("
                    f"(opening the condition expression) "
                    f"in if statement {statement}"
                    )
        # Parse expression
        statement += self.parse_expression()
        # Parse true codeblock
        statement += self.parse_codeblock()
        # Return if no statment
        token = self.next()
        if token[1] != 'else':
            self.back()
            return statement
        # Parse else
        statement += (token,)
        # Parse false codeblock
        return statement + self.parse_codeblock()

    def parse_while(self):
        # whileStatement:‘while' '(' expression ')' codeblock
        # Parse opening (
        token = self.next()
        if token[1] == '(':
            statement = (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"while followed by ( "
                    f"(opening the condition expression) "
                    f"in while statement {statement}"
                    )
        # Parse expression
        statement += self.parse_parameterPass(),
        # Parse codeblock
        return statement + self.parse_codeblock()

    def parse_do(self):
        # doStatement:   'do' identifier ('.' identifier)?
        #                     '(' parameterPass ';'
        # Parse identifier
        token = self.next()
        if token[0] != 'identifier':
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"'do' not followed by identifier"
                    f"(the name of the class or function) "
                    f"in do statement"
                    )
        statement = (token,)
        # Parse possible method
        token = self.next()
        if token[1] == '.':
            statement += (token,)
            token = self.next()
            if token[1] == 'identifier':
                statement += (token,)
            else:
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"subroutine name contains a . "
                        f"but it is not followed by an identifier"
                        f"(the name of the method) "
                        f"in do statement {statement}"
                        )
            token = self.next()
        # Parse opening (
        if token[1] == '(':
            statement += (token,)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"subroutine name not followed by ( "
                    f"(the opening of the subroutine parameters) "
                    f"in do statement {statement}"
                    )
        return statement + self.parse_parameterPass()

    def parse_return(self):
        # returnStatement:'return' expression? ';'
        token = self.next()
        if token[1] == ';':
            return (token,)
        else:
            self.back()
            return self.parse_expression(end=';')

    ###########################################################################
    # EXPRESSIONS
    ###########################################################################
    #
    # expression[end]   term (op term)* end
    # op:               '+' | '-' | '*' | '/' |
    #                   '&' | '|' |
    #                   '<' | '>' | '=' |
    # term              : integerConstant
    #                   | stringConstant
    #                   | 'true'|'false'|'null'|'this'
    #                   | identifier ('[' expression ']')?
    #                   | identifier ('.' identifier)? '(' parameterPass
    #                   | subroutineCall
    #                   | ('-' | '~')? term
    #                   | '(' expression ')'
    # [parameterPass]:  expressionList ')'
    # {expressionList}: (expression ',')* expression?

    def parse_expression(self, end=')', expressionList=False):
        # expression[end]   term (op term)* end
        # term              : integerConstant
        #                   | stringConstant
        #                   | 'true'|'false'|'null'|'this'
        #                   | ('-' | '~')? term
        #                   | '(' expression ')'
        #                   | identifier ('[' expression ']')?
        #                   | identifier ('.' identifier)? '(' parameterPass
        # op:               '+' | '-' | '*' | '/' |
        #                   '&' | '|' |
        #                   '<' | '>' | '=' |
        ops = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        # Start expression
        expression = ('expression', )
        while True:
            term = ('term',)
            token = self.next()
            # Parse constants
            if token[0] in ['integerConstant', 'stringConstant'] or \
               token[1] in ['true', 'false', 'null', 'this']:
                return term + (token,)
            # Parse unary operators
            if token[1] in ['-', '~']:
                return term + (token,) + (self.parse_term(),)
            # Parse term expression
            if token[1] in ['(']:
                return term + (token,) + (self.parse_expression(),)
            # Parse identifiers
            if token[0] != 'identifier':
                raise SyntaxError(
                        f"FAIL parsing token {token}: "
                        f"token does not start a term, "
                        f"expecting a constant, an identifier, "
                        f"-, ~, (, null or this"
                        )
            # From this point on we know we have an identifier, either
            #   - variable
            #   - array
            #   - class with method call
            #   - function call
            term += (token,)
            token = self.next()
            # Parse function call
            if token[1] == '(':
                return term + (token,) + self.parse_parameterPass()
            # Parse array
            if token[1] == '[':
                return term + (token,) + self.parse_expression(end=']')
            # Parse class.method call
            if token[1] == '.':
                term += (token,)
                # Parse method identifier
                token = self.next()
                if token[1] == 'identifier':
                    term += (token,)
                else:
                    raise SyntaxError(
                            f"FAIL parsing token {token}: "
                            f"subroutine name contains a . "
                            f"but it is not followed by an identifier"
                            f"(the name of the method) "
                            f"in subroutine call"
                            )
                # Parse opening (
                token = self.next()
                if token[1] == '(':
                    return term + (token,) + self.parse_parameterPass()
                else:
                    raise SyntaxError(
                            f"FAIL parsing token {token}: "
                            f"class.method not followed by ( "
                            f"(opening the parameters passed to the method) "
                            f"in subroutine call"
                            )
            # Otherwise we assume it is just a variable
            # and the term has ended
            expression += (term,)
            # Check for operator
            if token[1] in ops:
                expression += (token,)
            else:
                break
        # If more = True then we are parsing
        # an expression in an expression list
        if expressionList:
            # Check if there could be another expression after ,
            if token[1] == ',':
                return ((expression, token), True)
            # If no comma then there must be a closing )
            # (since we are here because the expression ended)
            if token[1] == ')':
                return ((expression, token), False)
            # If neither , or ) are found then there is a syntax error
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"expression not followed by , or ) "
                    f"in expression list"
                    )
        # If we are here then more = False
        # and we are parsing a single expression
        #   - array:
        #       '[' expression ']'
        #   - return and let assignment:
        #           expression ';'
        #   - term and if/while conditions:
        #       '(' expression ')'
        if token[1] == end:
            return (expression, token)
        else:
            raise SyntaxError(
                    f"FAIL parsing token {token}: "
                    f"terminating {end} expected "
                    f"after expression {expression}"
                    )

    def parse_parameterPass(self):
        # [parameterPass]:   expressionList ')'
        # {expressionList}:  (expression ',')* expression?
        # Actual implementation
        # [parameterPass]:   (expressionList ',')* expression ')'
        jack_list = ('expressionList',)
        # Parse parameters
        more = True
        while more:
            expression, more = self.parse_expression(expressionList=True)
            if more:
                jack_list += expression
            else:
                jack_list += expression[0]
                return (jack_list, expression[1])
        # Parse closing )
        # if token[1] == ')':
        #     return  (jack_list, token)
        # else:
        #     raise SyntaxError(
        #             f"FAIL parsing token {token}: "
        #             f"subroutine parameters not closed by ) "
        #             f"in subroutine declaration"
        #             f"{jack_class_subroutine}"
        #             )

# class Syntacker END
#   __init__(self,
#                  jack_filename,
#                  analyze = False,
#                  xml     = False,
#                  save    = False,
#                  strict  = True,
#                  ):


###############################################################################
# JACK TOKENIZER SCRIPT
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

    # COMPILE input file
    Syntacker(sys.argv[1], save=True)
