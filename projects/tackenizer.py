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
#   - strings and comments are part of syntax
#   - tokens generally come before syntax
#     but this does not work for strings and comments
#   - strings and comments behave somewhere in between tokens and syntax;
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

# Split the text into candidate tokens

# Logic:
#   - Strings are allowed white spaces, but any other white space separates tokens
#     Therefore we need to tokenize strings first and then the rest
#   - The rest is tokenized by spaces or symbols
#   - We inject spaces around every symbol
#   - Then everything that is not a string is tokenized by spaces


# Strings
# How to distinguish from the spaces to split?
# Proposal
#   - Split at double quotes
#       - splits = line.split('"')
#       - splits[0]  = '' if line starts with "
#       - splits[-1] = '' if line ends   with "
#       - consecutive " also produce '' in the middle
#     Therefore if the length of strings is even,
#     then there was an odd number of "
#   - raise an exception if len(splits) is even
#   - add the quotes back on the odd index entries

# Symbol separation translator
# We make sure every symbol is surrounded by spaces
# then splitting the string at spaces will isolate all symbol tokens
# The following is the translator to add these spaces
symbol_separator = {symbol: f" {symbol} " for symbol in TAGS['symbol']}

def token_separator(line):
    # We assume the line
    #   - has no newlines
    #   - has no comments
    #   - is not empty
    #   - has no leading and trailing spaces
    # Under this assumptions the only failure is an odd number of "

    # Split at "
    #   - there are always number of " + 1 splits
    #   - " are always inside the splits
    splits = line.split('"')
    # Throw error if there is an odd number of quotes
    # (an even number of quotes always produces an odd number of splits)
    if len(splits) % 2 == 0:
        raise SyntaxError("{line}: odd number of quotes")
    # Now
    #   - the number of splits is odd
    #   - the inside of quotes is at odd index
    #     (thus first and last split are never string tokens)
    #   - if line is not empty (which we assume)
    #     then len(splits) >=1
    # Check if the leading string is empty
    if splits[0] == "":
        # If line is not empty then len(splits) >=3
        # Remove leading empty string (now len(splits) >=2)
        splits = splits[1:]
        # Mark that string tokens start at 0
        strings = 0
    else:
        # Mark that string tokens start at 1
        string = 1
        # Make sure len(splits) stays even (now len(splits) >= 1)
        # because of the logic below processing in pairs
        # Check if the last split is empty
        if splits[-1] == "":
            # This only happens if len(splits) >=3
            # (otherwise we would satisfy splits[0] == "")
            # The last split is never a string
            # therefore if empty it can be removed (now len(splits) >=2)
            splits = splits[:-1]
        else:
            # If not empty then add '"'
            # !Do not add '', it will be treated as string
            #  and transformend into '""'
            # By adding '"', which is impossible to obtain in splits,
            # we can later check for '"""' and safely remove it
            splits = splits + ['"']
    # If the line was non empty, then at this point len(splits) >= 2
    # Start collecting tokens by splitting the rest
    tokens = []
    for i in range(0, len(splits), 2):
        # Splits the non strings into the rest of the tokens
        # (first put spaces around symbols and then split at spaces)
        splits[i + (not string)] = \
                splits[i + (not string)].translate(symbol_separator).split()
        # Add quotes back to the string tokens
        splits[i +      string ] = [f'"{splits[string + i]}"']
        tokens += splits[i] + splits[i + 1]
    # Finally remove the trailing empty string if there
    # (if tokens[-1] = '""' it means the jack code
    #  had an actual empty string token "" at the end of the line)
    if tokens[-1] == '"""':
        tokens = tokens[:-1]
    # Return the list of tokens
    return tokens




# Once symbols are separated
# keywords, integers and identifiers should be separated too
# because spaces are not allowed between them


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
    # We assume strings and symbols have been isolated 

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
    #  and quotes are even are not inside by construction)
    if token[0] == token[-1] == '"':
        return 'stringConst'

    raise ValueError(
            f"{token}: invalid Jack token\n"
            f"not a keyword, symbol, integer, string or valid identifier"
            )

################################################################################
# JACK TOKENIZER
################################################################################

def remove_jack_extension(jack_filename):
    if jack_filename[-5:] != ".jack":
        import warnings
        warnings.warn(f"Warning: extension of input file {jack_filename} is not '.jack'")
        return jack_filename
    else:
        return jack_filename[:-5]

def clean_line(line):
    # Remove comments
    line = line.split('//')[0]
    # Remove leading and trailing spaces
    # (leave inner spaces as they may be part of strings)
    return line.strip()

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
