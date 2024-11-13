## Regular expressions with `re`

**Regex Character Classes:**

shorthand | represents
-|-
`\d` | digits from 0 to 9
`\w` | all word characters (letters, digits, underscore)
`\s` | space, tab, ot newline character
`.*` | greedy wildcard (will match as much as possible)
`.*?` | non-greedy wildcard (will match shortest string)


**Assertions and variables**

syntax | effect | comments
-|-|-
`(?=foo)` | Positive lookahead |
`(?<!foo)` | Negative lookbehind | **Negative lookbehind can be concatenated**.  E.g.: *searching for a name, can use negative lookbehind to exclude both beginning of line and previous punctuation:* `nameMatchObject = re.compile(r'(?<!^)(?<!! )[A-Z][a-z]+')`
`re.compile(r'foo', re.DOTALL)` | match all characters  | if you want to capture newline character (`\n`)
`re.compile(r'foo', re.I)` | ignore case | if you want to ignore case, provide the argument
`re.compile(r'foo', re.VERBOSE)` | Verbose mode | if you want to provide a multi-line regex pattern, provide argument

**`sys` module**

To check if the CLI input is more than just the command, and concatenate all arguments provided as one flag:
```
import sys
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
```
