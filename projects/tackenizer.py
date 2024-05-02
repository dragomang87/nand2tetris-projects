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
# JACK TOKEN SPLITTER
################################################################################

# HYBRID TOKENIZER

# We use a dictionary as a functionto tokenize
# The advantage is that we let the dictionary match what we are tokenizing
# while we just treat the line always in the same way
# (we use the dictionary keys instead of if statements)
# Output: a tuple of size two containing
#   - the token
#   - the rest of the line
# Logic:
#   - in case of symbols or delimiters we passed the rest of the line
#   - in case of 'other' tokens we pass the whole line including the token
#   - in case of comments the token is None
#   - in case of unterminated block comment, the rest of the line is None
#     in all other cases it is a string
# In case of comments the token is None
TOKEN_SEPARATOR = {}

# Comments
# If inline comment then absorb the whole line
# The token is None and the rest of the line is empty
TOKEN_SEPARATOR['//'] = lambda line: (None, '')
# If block comment then absorb until */
# The token is None and without */ then the rest of the line is also None
# to signal that the block comment is not closed
split_or_nothing = lambda split: None if len(split) == 1 else split[1].strip()
TOKEN_SEPARATOR['/*'] = lambda line: (None,
        split_or_nothing(line.split('*/', maxsplit=1))
        )

# Symbols
# Just return the symbol and the line, nothing to do
for symbol in TAGS['symbol']:
    TOKEN_SEPARATOR[symbol] = lambda line: (symbol, line.strip())

# Strings
# We assume the leading quote has been stripped
# and we assume the string is closed by assuming the split has length 2
# If there is no quote and the split has length 1
# then this is a syntax error and we don't stop the exception cause by split[1]
quote_and_strip = lambda split: ('"' + split[0] + '"', split[1].strip())
TOKEN_SEPARATOR['"'] = lambda line: quote_and_strip(line.split('"', maxsplit=1))

# Numbers, Keywords and Identifiers
# If we are expectin a number, keyword or identifier
# then just take the first piece up to the next space
# This assumes that we have already tested for comments, symbols and strings
# Logic:
#   - use split() and maxsplit=1 to split at the first space only
#   - using the default separator=None automatically strips
#     the spaces from both line and split[0] and split[1]
#     (as opposed as the separator for symbols that calls strip() explicitly)
split_or_everything = lambda split: split if len(split) == 2 else split + ['']
TOKEN_SEPARATOR['other'] = lambda line: split_or_everything(line.split(maxsplit=1))


#def token_separator(line):
def separate_line(line):
    tokens = []
    while line:
        # Check if starting with // or */
        if line[:2] in TOKEN_SEPARATOR:
            _, line = TOKEN_SEPARATOR[line[:2]](line[2:])
            continue
        # Check if starting with symbol or "
        if line[:1] in TOKEN_SEPARATOR:
            try:
                token, line = TOKEN_SEPARATOR[line[:2]](line[2:])
            except IndexError as e:
                raise("{line}: string missing end quote \"") from e
            tokens +=[token]
            continue
        # In all other case separate until next space
        token, line = TOKEN_SEPARATOR['other'](line)
        tokens += [token]
    # Return the list of tokens and the status of the line
    # (there will be either '' or None
    # depending on whether there is an open block comment)
    return tokens, line







# OTHER FAILED LOGICS




# TRUE-TOKENIZER LOGIC
# Spaces and comment delimiters should be kept as tokens
# The abstract tree should be take care of interpreting
# when comments and strings start and end
# Advantage: comments can be added in debug compiled code
# Logic:
#   - we cannot use spaces as separators anymore
#   - newlines are always removed because they are not allowed in strings
#   - we can use newlines instead of spaces to separate symbols
#     (because otherwise )
# Problems
#   - translators can only translate single characters
#   - //, /* and */ are compositions of / and *
#     therefore the translator for / and * will inject
#     newlines in between //, /* and */
#   - this translator injects the newlines
#       newline_injector =
#           {ord(symbol): f"\n{symbol}\n" for symbol in TAGS['symbol'] + ['"']}
#     (translators need the character ascii/unicode number,
#     therefore we need to use ord(character) instead of character as key)
#   - we still need to separate using spaces because there is no way
#     to correctly introduce newlines between words and spaces
#   - consecutive spaces then need to be joined back together





# NO-COMMENTS LOGIC
# Split the text into candidate tokens assuming no comments
#   - Strings are allowed white spaces, but any other white space separates tokens
#     Therefore we need to tokenize strings first and then the rest
#   - The rest is tokenized by spaces or symbols
#   - We inject spaces around every symbol
#   - Then everything that is not a string is tokenized by spaces
# This only works if comments are already removed
# Implementation:
#   - Split at double quotes
#       - splits = line.split('"')
#       - splits[0]  = '' if line starts with "
#       - splits[-1] = '' if line ends   with "
#       - consecutive " also produce '' in the middle
#     Therefore if the length of strings is even,
#     then there was an odd number of "
#   - raise an exception if len(splits) is even
#   - add the quotes back on the odd index entries
#   - for the other entries apply the translator
#     symbol_separator = {symbol: f" {symbol} " for symbol in TAGS['symbol']}
#     this translator surrounds every symbol by spaces
#   - then splitting the string at spaces will isolate all symbol tokens
# Failures:
#   - comments can "disable" quotes
#   - quotes can disable comments
#   - therefore strings and comments have to be tokenized at the same time



################################################################################
# JACK TOKEN CLASSIFIER
################################################################################

# Keyword/Symbol classifier
# We classify keywords and symbols by using the reverse of the TAGS dictionary
# (defining TAGS first and TOKENS as the reverse
#  saves us from repeatedly writing 'keyword' and 'symbols' above)
TOKENS = {token: tag for tag in TAGS for token in TAGS[tag]}

# Identifier reverse translator
# We check if a string is an identifier
# by removing all the valid symbols
# and checking for the empty string
# The following is the translator to make this removal
identifier_characters = ( # map ASCII codes to empty string
        # digits     ['0','9'] = [48, 57[
        {code: "" for code in range(48, 58)} |
        # uppercase  ['A','Z'] = [65, 91[
        {code: "" for code in range(65, 91)} |
        # lowercase  ['a','z'] = [97,123[
        {code: "" for code in range(97,123)} |
        # underscore
        {ord("_"): ""}
        )

def classify(token):
    # We assume tokens have been isolated by the previous process

    # Check if keyword or symbol
    if token in TOKENS:
        return TOKENS[token]

    # Check if integer
    try:
        int(token)
        return 'intConst'
    except:
        pass

    # Check if identifier by
    #   - checking that removing identifier_characters we get the empty string
    #   - the first character is not a digit
    if token.translate(identifier_characters) == "" and token[0] not in "0123456789":
        return 'identifier'

    # Check if string
    # (newlines have been removed with the spaces
    #  and quotes are even and not inside by construction)
    if token[0] == token[-1] == '"':
        return 'stringConst'

    raise ValueError(
            f"{token}: invalid Jack token\n"
            f"not a keyword, symbol, integer, string or valid identifier"
            )

################################################################################
# JACK TOKENIZER
################################################################################

#lines = iter(cdata.splitlines())
#for line in lines:
#    if exp.match(line):
#       #increment the position of the iterator by 5
#       for _ in itertools.islice(lines, 4):
#           pass
#       continue # skip 1+4 lines
#    print line

def remove_jack_extension(jack_filename):
    if jack_filename[-5:] != ".jack":
        import warnings
        warnings.warn(f"Warning: extension of input file {jack_filename} is not '.jack'")
        return jack_filename
    else:
        return jack_filename[:-5]

tag_token = lambda token, tag: (
        f"<{tag}> {token} </{tag}>\n"
        )

def tokenize(jack_filename, debug=True):
    # Get output filename
    tokens_filename = remove_jack_extension(jack_filename) + ".jacken"
    if debug: print(f"Compiling file {jack_filename} into {tokens_filename}")
    # Tokenize
    with open( jack_filename, 'r') as jack, \
         open(tokens_filename, 'w') as tokens_file:
        # Keep track of if we are waiting to close a block comment or not
        block_comment = False
        last_block_comment_start = 0
        # Loop over lines
        for (line_number, line) in enumerate(jack, 1):
            # Things to keep track of
            #   - comments and strings can disable each other:
            #     // or /* inside a string are not comments and
            #     "  inside a comment is not a string
            #   - block comments spill over to other lines
            # Logic:
            #   - we need different parsing modes:
            #       string
            #       comment
            #       block comment
            #       easy tokens (tokens not interfering with each other
            #                    outside of strings and comments)
            #   - need to have a variable to keep track
            #     if we are still in a block comment at the next line
            # Remove leading and trailing spaces
            # (leave inner spaces as they may be part of strings)
            line = line.strip()
            while line: # not empty
                # REMOVE COMMENTS
                # Comment logic:
                #   - clean line before for "//" to invalidate "/*" or "*/"
                #   - clean line after  if  "/*" or "*/" can work after "//"
                # Remove inline comments, leading and trailing spaces
                line = clean_line(line)
                # Skip block comment
                if block_comment:
                    if "*/" in line:
                        # Keep only what's after the last "*/"
                        line = line.split("*/")[-1]
                    else:
                        # Do not process if line is in block comment
                        # and there is no closing "*/"
                        continue
                # Check for start of block comment
                # Need to check if it closes and opens again in the same line
                if "/*" in line:
                    # Then split at /*
                    line = line.split("/*")
                    # Then check if each piece has a closing */
                # PROCESS LINE
                # Ignore empty lines
                # (need to check after block comments are processed)
                if line == '': continue
                # Try to separate the tokens
                try:
                    tokens = token_separator(line)
                    if debug: print(
                            f"Separating tokens in line {line_number}: '{line}'"
                            )
                except Exception as e:
                    raise Exception(
                            f"Separating tokens in line {line_number} FAILED: '{line}'"
                            ) from e
                # Try to classify tokens
                try:
                    tags = [tag_token(token, classify(token)) for token in tokens]
                    [tokens_file.write(tag) for tag in tags]
                    if debug: print(
                            f"Tokenizing line {line_number}: '{line}' -> {tokens}"
                            )
                except Exception as e:
                    raise Exception(
                            f"Tokenizing line {line_number} FAILED: '{line}' -> {tokens}"
                        ) from e
    return tokens_filename


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
    tokenize(sys.argv[1])
