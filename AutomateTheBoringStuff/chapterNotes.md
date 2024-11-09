# Automating the boring stuff
## Chapter 1: Python programming basics
**Expression vs statement**: an expression is a combination of values and operators. All expressions evaluate (i.e. reduce) to a single value, statements do not.

## Chapter 2: Flow control
**Condition**: A condition is an expression used in a flow control statement that evaluates to a Boolean value.  
**Break vs continue statements**: The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.

## Chapter 3: Functions
The data type of `None` is `NoneType`.  
Can use the `global` statement to modify a global variable from within a function. eg:
```
def spam()
  global eggs
  eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
```
Output: `spam`  
Exception handling: to avoid program crash from errors/exceptions, do `try` and `except` clauses. Eg: `except ZeroDivisionError`

## Chapter 4: Lists
NB: slice of a list will include the first item, but will go up (not including) the second item. `spam[1:3]` grabs `spam[1]` and `spam[2]`.  
Multiple assignment trick: can assign a list as a value for three variables. Make sure to have the same number of variables and items in the list or you'll get a `ValueError`
```
cat = [tuxedo, tabby, Sphynx]
Twist, Daisy, Ramses = cat
```
**Method vs function**: method is same as a function, except it is "called on" a value. Difference between `cat.index(tuxedo)` vs `print(cat[0])`  
Modify lists *in place* with `myList.insert(index, itemToInsert)` and `myList.append(itemToInsert)`.  
Can also remove items with `myList.remove(itemToRemove)`  
**List-like data types**: strings and tuples. 
- String vs list: a list is a **mutable** data type and strings are basically lists of characters.
- Tuples vs lists: Tuples are types with parentheses, Also, tuples cannot have their values modified/appended/removed. Finally, using tuples is slightly faster.

**⚠References**: be careful when making a copy of a list, because modifying either list will affect the other. **When you assign a list to a variable, you are actually assigning a list reference to the variable.** Essentially, when copying a list, they both point to the same sequence of values. eg:
```
cats = ["tuxedo", "tabby", "Sphynx"]

catsCopy = cats

catsCopy
Out[4]: ['tuxedo', 'tabby', 'Sphynx']

cats[1] = "orange"

catsCopy
Out[6]: ['tuxedo', 'orange', 'Sphynx']
```
To avoid modifying the original list or dictionary, you can use the module `copy` which includes functions `copy()` and `deepcopy()` (the latter is used for embedded lists).

> "The del statement is good to use when you know the index of the value
you want to remove from the list. The remove() method is good when you
know the value you want to remove from the list." (p. 91)

## Chapter 5: Dictionaries and Structuring Data

`keys(), values(), items()`: values returned are not true lists but they can be used in `for` loops. NB: values returned by `items()` method are tuples.  
Can use get() method on dictionary to retrieve value based on key. get() takes two arguments: the key you are searching for, and a default value if the key doesn't exist.  
Use `setdefault` to create a key value if the key does not exist already. If it does exist, it will return the current value. Can use it to create a character counter for example:
```
count = {}
string = "foo bar baz"
for character in message:
    count.setdefault('character', 0)
	count[character] += 1
``` 

Can pretty print a dictionary to make it easier to read using `pprint` and `pformat`

## Chapter 6: Manipulating Strings
Use raw strings to enable the use of *escape characters* (`\`, `\t`, `\n`, `"`, `'`). eg: `r"This is a raw string so I can use \"`  

**String methods**:
- methods to convert: `upper()`, `lower()`
- `is` methods to check content of string: `isupper()`, `islower()`, `isalpha()`, `isalnum()`, `isdecimal()`, `isspace()`, `istitle()`
- `join()` and `split()` (NB: `join` follows the separator eg `' '.join(listOfStrings)`, while `split` follows the string you are splitting eg `"My name is Ben".split()`)
- Can justify text to the left, right, or center: `ljust()`, `rjust()`, `center()`. Can be useful to output item lists/receipts.
- remove whitespace with `strip()`, `rstrip()` and `lstrip()`. Whitespace by default but can choose any characters to strip - order doesn't matter i.e. `myString.strip('Spam')` is equivalent to `myString.strip('ampS')`.
- Can import the module **`pyperclip`** (doesn't come by default) to copy and paste things to the clipboard: `pyperclip.copy(myString)`, `pyperclip.paste()`.

## Chapter 7: Pattern Matching with Regular Expressions
Can pass a raw string regex pattern to a `re.compile` object. Will return a **regex pattern object**.
```
phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
```
- if want to capture newline character (`\n`), provide `re.compile()` the argument `re.DOTALL`
- if you want to ignore case, provide the argument `re.I`
- if you want to provide a multi-line regex pattern, provide argument `re.VERBOSE`

Can combine the arguments using a *bitwise operator* `|`:
```
someRegexValue = re.compile('foo', re.I | re.DOTALL | re.VERBOSE)
```
**N.B.** for complex regex searches use `VERBOSE` and comments:
```
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?		# area code
	(\s|-|\.)? 			# separator
	\d{3} 				# first 3 digits
	(\s|-|\.) 			# separator
	\d{4} 				# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?	# extension
	)''', re.VERBOSE)
```

Use `.search()` method on the regex object and pass a string value to find matches. NB search returns the first result. If you want to find all matches, use `findall()`.
```
matchObject = phoneNumberRegex.search("My number is 415-555-4242.")
```
If a match is found, can output the matched sub-string with `.group()`:
```
matchObject.group()
```
If you are using capture groups `()` in your regex pattern, `.group()` can return either the entire match with `.group()` or `.group(0)`, or your capture group `.group(1)`.
```
>>> regexPattern = re.compile(r'(\d{3})-(\d{3}-\d{4})')
>>> phoneNumberMatch = regexPattern.search("202-805-8085")
>>> phoneNumberMatch.group()
'202-805-8085'
>>> phoneNumberMatch.group(1)
'202'
```
The `findall()` method returns a list of strings with every match in the searched string. **N.B.** if you use the `.findall()` method with capture groups, it will return a list of tuples of strings.
```
>>> regexPattern = re.compile(r'(\d{3})-(\d{3}-\d{4})')
>>> phoneNumberMatch = regexPattern.search("Call is 202-805-8085, home is 212-628-7724")
>>> phoneNumberMatch.group()
'202-805-8085'
>>> phoneNumberMatch.group(1)
'202'
>>> phoneNumberMatch.group(2)
'805-8085'
>>> AllPhoneNumberFound = regexPattern.findall("Cell is 202-805-8085, home is 212-628-7724")
>>> AllPhoneNumberFound
[('202', '805-8085'), ('212', '628-7724')]
>>> regexPatternNoGroup = re.compile(r'\d{3}-\d{3}-\d{4}')
>>> AllPhoneNumberFoundNoGroup = regexPatternNoGroup.findall("Cell is 202-805-8085, home is 212-628-7724")
>>> AllPhoneNumberFoundNoGroup
['202-805-8085', '212-628-7724']
```
**Regex Character Classes:**

shorthand | represents
-|-
\d | digits from 0 to 9
\w | all word characters (letters, digits, underscore)
\s | space, tab, ot newline character

Make your own character class: 
```
vowelRegex = re.compile(r'[AEIOUaeiou]')
```
**substitute strings** using the `.sub()` method:
```
>>> agentNameRegex = re.compile(r'Agent \w+')
>>> agentNameRegex.sub("CENSORED", "Agent Ben gave Agent Marina a very important loaf of bread")
'CENSORED gave CENSORED a very important loaf of bread'
```
Your wildcard `.*` can be greedy and will match as much as possible, or **non-greedy** and match the shortest string `.*?`.

**Additional notes:**  
Lookahead: `(?=foo)`
Negative lookbehind: `(?<!foo)`
- **N.B.** Negative lookbehind can be concatenated.  
```
nameMatchObject = re.compile(r'(?<!^)(?<!! )[A-Z][a-z]+')
```
> *searching for a name, can use negative lookbehind to exclude both beginning of line and previous punctuation*


## Chapter 8

`os` functions | usage
-|-
`os.getcwd()` | Get current working directory.
`os.chdir()` | Change working directory
`os.makedirs()` | Create folder
|
`os.path.join()` | Provide directory names and filename as arguments. Attaches argument strings together based on OS. 
`os.path.abspath(path)` | Get the absolute path of the arg. eg: `os.path.abspath('.')`
`os.path.isabs(path)` | Boolean; True is arg is absolute path. False if relative.
`os.path.relpath(path, start)` | Returns string of relative path from `start` to `path`. Will assume current working directory is start if none is provided.
`os.path.basename(path)` | will provide string of everything the **after** last slash in the `path` argument.
`os.path.dirname(path)` | will provide string of everything **before** the last slash in the `path` argument.
`os.path.split(path)` | will provide tuple of two strings, one for before last slash, one for after.
|
`os.path.getsize(path)` | returns the size in bytes of the file in `path` arg. To get folder size of `currentPath`, iterate over all filenames in `os.listdir(currentPath)` and add up `os.path.getsize(os.path.join(currentPath,filename)`
`os.listdir(path)` | returns the list of filename strings for each file in the `path` arg.
|
`os.path.isdir()` | Boolean; return True if path exists and is directory.
`os.path.isfile()` | Boolean; return True if path exists and is file.
`os.path.exists()` | Boolean; return True if path to file or directory. exists.
|

### Use `os` to avoid issues between Linux and Windows
To avoid Linux vs Windows path issues, avoid hardcoding `\` for Windows or `/` for Linux.  
Can use `os.path.sep` object to get the directory separator used by current OS:
```
>>> filepath = 'C:\\Windows\\System32\\calc.exe'
>>> filepath.split(os.path.sep)
['C:', 'Windows', 'System32', 'calc.exe']
```
Three steps of handling a file:
- `open('filepath', <mode>)` the file to create a file object. By default opens in **read mode** (`'r'`).  Can also open in **append mode** (`'a'`) and **write mode** (`'w'`)
- `read()` or `write()` the file object. 
  - Can use `readlines()` instead of `read()` to get a list of strings instead of a whole string of the text.
- `close()` the file

### Saving variables with `shelve` module

You can save variables into files using `shelve`.  
This can be useful if you're saving parameters or configurations from your Python script, especially if the data is not meant to be read as a text file.
```
import shelve
shelfFile = shelve.open('mydData')
dataList = ["alpha", "bravo", "charlie"]
shelfFile[data] = dataList
shelfFile.close()
``` 
You can then access the keys and values of your shelf file. Since they are "list-like" values, use `list()`: `list(shelfFile.keys())`, `list(shelfFile.values())`.

### Using `pprint.pformat()` to save variables

You can use pprint.pformat() to save variables to a file in a legible *and* python-friendly way.
```
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py', 'w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close()
```
> code above will create a file named "mycats.py" which contains a single line `cats = [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]`

You can use `pprint.pformat()` to create new python files, which can in turn be imported:
```
>>> import myCats
>>> myCats.cat
[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
```

## Chapter 9: Organizing Files

### The `shutil` module
"Calling `shutil.copy(source, destination)` will copy the file at the path
source to the folder at the path destination"

`shutil.copytree()` will copy an entire folder and every folder and file contained in it.

`shutil.move(source, destination)` moves source file or folder to destination. NB: can overwrite, or be used to rename a file.

**deleting files and paths**:
- `os.unlink(path)` will delete the file at path.
- `os.rmdir(path)` will delete the folder at path. This folder must be
empty of any files or folders.
- `shutil.rmtree(path)` will remove the folder at path, and all files
and folders it contains will also be deleted.

**Can safe delete using `send2trash` Module**. This will send files to the recycle bin instead of deleting them forever.

### Walking a directory tree:

Can loop through folder, subfolders, and files in `os.walk("path")`.
```
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
	print('The current folder is ' + folderName)
	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': '+ filename)
```
> `os.walk()` will return three values on each iteration through the loop: 1. A string of the current folder’s name, 2. A list of strings of the folders in the current folder, 3. A list of strings of the files in the current folder

### Compressing Files with the zipfile Module
To read the contents of a ZIP file, first you must create a `ZipFile` object with `zipfile.ZipFile()` 

ZipFile objects methods: 
- `namelist()`: returns a list of strings for all the files and folders contained in the ZIP file.
- `getinfo()`: creates ZipInfo objects that have their own attributes, such as `file_size` and `compress_size` in bytes
- `extractall()` will open zip file and copy all files to current working directory. Can also pass a string to a new destination path.
- `extract("fileToExtract")` for a single file to be extracted.

To create a zip file, you need to create a ZipFile object in write mode: `newZip = zipfile.ZipFile('new.zip', 'w')`

## Chapter 10: Debugging

### Raising Exceptions
**An exception is raised whenever Python tries to execute invalid code**
```
>>> raise Exception('This is the error message.')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: This is the error message.
```
> `raise` statements consists of: `raise` keyword, a call to the `Exception()` function, a helpful message passed as a string.

**Best practice:** a raise statement inside a function, and the try and except statements in the code calling the function.
```
def myFunction(foo, bar, baz):
    if len(foo) != 1:
        raise Exception('Foo must be a single character string.')
    print(bar * baz)

try:
    boxPrint(sym, w, h)
except Exception as err:
    print(f"An exception happened: {str(err)}")
```
> If an `Exception` object is returned from `myFunction()`, the `except` statement will store it in a variable named `err`

### Getting the Traceback as a String
Traceback is the information yielded when Python encounters an error. It includes the  error message, line number, and the sequence of calls that lead to the error (*call stack*).

You can get the traceback info as a string with `traceback` module: `traceback.format_exc()`. 
```
>>> try:                                         e")
	raise Exception("This is the error message")
except:                                      e")
	with open("errorInfo2.txt", 'w') as errorLog:
		errorLog.write(traceback.format_exc())
```
> Instead of crashing program when an exception occurs, write to a log file and keep program running.

### Assertions
**An *assertion* is a sanity check performed by `assert` statements.**
```
>>> podBayDoorStatus = "I'm sorry, Dave. I'm afraid I can't do that"
>>> assert podBayDoorStatus == "open", "The pod bay doors need to be 'open'."
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: The pod bay doors need to be 'open'.
```
> Assertion consists of: `assert` keyword, a condition, a comma, a string to display when condition is `False`

Unlike exceptions, your code *should not* handle assertions: if an assertion fails, the code should crash (fail fast).
**Assertions are for programmer errors, not user errors**

Can disable assertions at runtime by passing the `-0` option 

### Logging

`logging` module:
When Python logs an event, it creates a `LogRecord` object that holds information about that event.  
The `logging` module’s `basicConfig()` function lets you specify what details about the LogRecord object you want to see and how you want those details displayed.
```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
```
> `debug()` function will call `basicConfig()`, a line of info will be printed.


**Logging levels:**
Pass different values to `logging.basicConfig(level=)` to calibrate the amount of info you wish to see. 

Level | Logging function | Description
-|-|-
DEBUG | `logging.debug()` | The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
INFO | `logging.info()` | Used to record information on general events in your program or confirm that things are working at their point in the program.
WARNING | `logging.warning()` | Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
ERROR | `logging.error()` | Used to record an error that caused the program to fail to do something.
CRITICAL | `logging.critical()` | The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely

Can disable subsequent logs with `logging.disable(logging.CRITICAL)` (or with any other level).

Can log to a file with `filename` keyword argument of `logging.basicConfig()` function. eg: `logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')`

### Debugger

Based on IDLE debugger functionalities:
- Go: code executes until it reaches a **breakpoint**
- Step: execute next line of code then pause again. If code is a function call, will "step into" the function and go to the first line of said function.
- Over: similar to step, except it will "step over" a function call and execute it.
- Out: execute all lines of code until you have stepped out of the function you're in.
- Quit: terminates program