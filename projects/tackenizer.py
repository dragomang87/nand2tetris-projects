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
# JACK TOKEN CLASSIFIER
################################################################################

# Keyword/Symbol classifier
# We classify keywords and symbols by using the reverse of the TAGS dictionary
# (defining TAGS first and TOKENS as the reverse
#  saves us from repeatedly writing 'keyword' and 'symbols' above)
TOKENS = {token: tag for tag in TAGS for token in TAGS[tag]}

# Identifier erase translator
# We check if a string is an identifier
# by removing all the valid symbols
# and checking for the empty string
# The following is the translator to make this removal
identifier_eraser = ( # map ASCII codes to empty string
        # digits     ['0','9'] = [48, 57[
        {code: "" for code in range(ord('0'), ord('9') + 1)} |
        # uppercase  ['A','Z'] = [65, 91[
        {code: "" for code in range(ord('A'), ord('Z') + 1)} |
        # lowercase  ['a','z'] = [97,123[
        {code: "" for code in range(ord('a'), ord('z') + 1)} |
        # underscore
        {ord('_'): ""}
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
    #   - checking that removing identifier_eraser we get the empty string
    #   - the first character is not a digit
    if token.translate(identifier_eraser) == "" and token[0] not in "0123456789":
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
# JACK TOKEN SPLITTER
################################################################################

# HYBRID TOKENIZER

# We use a dictionary as a function to tokenize
# The advantage is that we let the dictionary match what we are tokenizing
# while we just treat the line always in the same way
# (we use the dictionary keys instead of many if statements)
# Output: a tuple of size two containing
#   - the token
#   - the rest of the line
# Logic:
#   - to separate symbols we inject newlines
#     these are then automatically removed by splitting
#     or in the case of strings they are manually removed
#   - the rest of the line we return it always stripped
#   - what we pass to the separator depends on the type
#   - in case of symbols we pass the whole line,
#     because of the limitation described below defining the lambda function
#   - because the string separator is also matched by a single character
#     we treat it like a symbol and pass the whole string
#   - in case /* comments we assume /* has been stripped
#     because we also use it in case of open comments
#     where there is no starting /*,
#     thus we leave it to the calling code to pass the whole line
#     or the line stripped of /*;
#     the output of unclosed block comments is None,
#     to be distinguished from '' which is the output of a fully parsed line
#   - in case of // comments it does not matter because everything is ignored
#     the output of the rest of the line is '' and the token is None
#   - in case of 'other' tokens we pass the whole line including the token
# In case of comments the token is None
TOKEN_SEPARATOR = {}

# Comments
#   - newlines have been injected to separate symbols
#     therefore we need to match /\n\n/, /\n\n* and *\n\n/
#   - if inline comment then absorb the whole line;
#     the token is None and the rest of the line is empty
TOKEN_SEPARATOR['/\n\n/'] = lambda line: (None, '')
#   - if block comment then absorb until *\n\n/,
#     the token is None and without *\n\n/ then the rest of the line is also None
#     to signal that the block comment is not closed
#   - we assume that '/\n\n*' has been stripped from the line
#     beause we use this to also parse open block comments
split_or_nothing = lambda split: None if len(split) == 1 else split[1].strip()
TOKEN_SEPARATOR['/\n\n*'] = lambda line: (None,
        split_or_nothing(line.split('*\n\n/', maxsplit=1))
        )

# Symbols
# We assume that the symbol is still present in the line
# (we cannot use the variable symbol in the for loop inside the lambda)
# Just return the symbol and the line, nothing to do
for symbol in TAGS['symbol']:
    TOKEN_SEPARATOR[symbol] = lambda line: (line[0], line[1:].strip())

# Strings
#   - we assume the leading quote is still there, like for symbols
#     therefore we split line[1:] and not just line
#   - we assume the string is closed by assuming the split has length 2
#     (this is implicit in the fact that we access split[1] without check);
#     if there is no quote and the split has length 1
#     then this is a syntax error and we don't stop the exception cause by split[1],
#     it will be handled by the line separator
#   - we put the quotes back into the string if the command succeeds
#     because the quote is used by the tokenizer to tag strings correctly
#   - we remove all the newlines from the string token
#     because no newlines are allowed and if there were any
#     they have been injected by the line separator to handle symbols
quote_and_strip = lambda split: (
        '"' + split[0].replace("\n", "") + '"',
        split[1].strip(),
        )
TOKEN_SEPARATOR['"'] = lambda line: quote_and_strip(line[1:].split('"', maxsplit=1))

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

# Newline injector
# This separator adds newlines around symbols and " so that the 'other' separator
# does not parse them as part of keywords, number and identifiers
# In case of strings we can easily remove the newlines in the token
# since no newlines are allowed in strings
newline_injector = {ord(symbol): f"\n{symbol}\n" for symbol in TAGS['symbol'] + ['"']}

def separate_line(line):
    # Separate symbols and " with newlines and strip
    # (remove leading and trailing spaces)
    # Do not strip before injecting because the injection can add leading newlines
    # (we leave inner spaces as they may be part of strings)
    line = line.translate(newline_injector).strip()
    tokens = []
    while line:
        # Check if starting with /\n\n/ or *\n\n/
        # We cannot use an if statement to check line[:4]
        # because there might not be a line[:4]
        try:
            _, line = TOKEN_SEPARATOR[line[:4]](line[4:])
            continue
        except:
            pass
        # Check if starting with symbol or "
        # (we can use an if statement because we know line is not empty)
        if line[0] in TOKEN_SEPARATOR:
            # If this fails then it must have matched a string
            # because the symbols token separator just returns the arguments
            try:
                token, line = TOKEN_SEPARATOR[line[0]](line)
            except IndexError as e:
                raise("{line}: string missing end quote \"") from e
            tokens += [token]
            continue
        # In all other case separate until next space
        # (this should also never fail)
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

xml_token = lambda token, tag: (
        f"<{tag}> {token} </{tag}>\n"
        )

TOKEN_SEPARATOR[None] = (None, None)

def tokenize(jack_filename, debug=True):
    # Get output filename
    tokens_filename = remove_jack_extension(jack_filename) + ".jacken"
    if debug: print(f"Compiling file {jack_filename} into {tokens_filename}")
    # Tokenize
    with open(  jack_filename, 'r') as jack, \
         open(tokens_filename, 'w') as tokens_file:
        # Things to keep track of
        #   - comments and strings can disable each other:
        #     // or /* inside a string are not comments and
        #     "  inside a comment is not a string
        #   - block comments spill over to other lines
        # Logic:
        #   - the line separators remove comments
        #     and returns the tokens and None
        #     if a block comment was left open
        #   - if line is None keep eating lines until
        #     TOKE_SEPARATOR['/*'] stops returning None
        #   - we meddle with the iterator enumerate(jack, 1)
        #     to manually skip lines inside the loop
        #     when a block comment is open
        # Implementation:
        #   - we loop over
        #       lines = iter(enumerate(jack, 1))
        #     instead of just
        #       enumerate(jack, 1)
        # Keep track of if we are waiting to close a block comment or not
        open_block_comment = False
        # Loop over lines
        for (line_number, line) in enumerate(jack, 1):
            # SEPARATE LINE
            if debug: print(f"Separating line {line_number}: '{line[:-1]}'")
            # Separate open block comment
            if open_block_comment:
                # Parse block comment
                _, line = TOKEN_SEPARATOR['/*'](line)
                # If the block comment is not terminated
                # then line is returned to be None
                if line is None:
                    continue
                else:
                    open_block_comment = False
            # Separate remaining line
            try:
                line_tokens, line = separate_line(line)
            except Exception as e:
                raise Exception(
                        f"Separating line {line_number} FAILED: '{line[:-1]}'"
                        ) from e
            # If a block comment was opened and not closed
            # then line is None and we mark it open
            if line is None:
                open_block_comment = True
            # TOKENIZE LINE
            # (need to check after block comments are processed)
            # Try to separate the tokens
            # Try to classify tokens
            if debug: print(f"Tokenizing line {line_number}: {line_tokens}")
            try:
                tag_tokens = [(token, classify(token)) for token in line_tokens]
                if debug: print( f"Tokens   line {line_number}: {tag_tokens}")
                xml_tokens = [xml_token(*tag) for tag in tag_tokens]
                if debug: print( f"XML tags line {line_number}: {xml_tokens}")
                [tokens_file.write(xml)       for xml in xml_tokens]
            except Exception as e:
                raise Exception(
                        f"Tokenizing line {line_number} FAILED: {line_tokens}"
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
