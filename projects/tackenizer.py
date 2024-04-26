################################################################################
# JACK TOKENS
################################################################################

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
        token = token[:-1]
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

    # Check if keyword or symbol
    if token in TOKENS:
        return TOKENS[token]

    # Check if integer
    try
        int(token)
        return 'intConst'
    except:
        pass

    # Check if identifier by
    #   - checking that removing identifier_characters we get the empty string
    #   - the first character is not a digit
    if not token.translate(identifier_characters)
    and token[0] not in [str(digit) for digit in range(10)]:
        return 'identifier'

    # Check if string
    # (newlines have been removed with the spaces)
    if token[0] == token[-1] == '"' and '"' not in token[1:-1]:
        return 'stringConst'

    except ValueError(
            f"{token}: invalid Jack token\n"
            f"not a keyword, symbol, integer, string or valid identifier"
            )

################################################################################
# JACK TOKENIZER
################################################################################

def remove_jack_extension(jack_filename):
    if vm_filename[-5:] != ".jack":
        import warnings
        warnings.warn(f"Warning: extension of input file {jack_filename} is not '.jack'")
        return vm_filename
    else:
        return vm_filename[:-5]

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
    tokens_filename = remove_vm_extension(jack_filename) + ".jacken"
    if debug: print(f"Compiling file {jack_filename} into {token_filename}")
    # Tokenize
    with open( jack_filename, 'r') as jack, \
         open(token_filename, 'w') as tokens_file:
        # Loop over lines
        for (line_number, line) in enumerate(jack, 1):
            # Remove comments, leading and trailing spaces
            line = clean_line(line)
            # Ignore empty lines
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
