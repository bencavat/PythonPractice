## Regular expressions with `re`

**Regex Character Classes:**

shorthand | represents
-|-
\d | digits from 0 to 9
\w | all word characters (letters, digits, underscore)
\s | space, tab, ot newline character

- Lookahead: `(?=foo)`
- Negative lookbehind: `(?<!foo)`
- **Negative lookbehind can be concatenated**.  
```
nameMatchObject = re.compile(r'(?<!^)(?<!! )[A-Z][a-z]+')
```
> *searching for a name, can use negative lookbehind to exclude both beginning of line and previous punctuation*

Your wildcard `.*` can be greedy and will match as much as possible, or **non-greedy** and match the shortest string `.*?`.
