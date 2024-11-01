# decorators.py
"""
Decorator practice file.
require_alpha input decorator function that loops until someone provides an aphabetical string
"""
from functools import wraps

def require_alpha(func):
    @wraps(func)
    def wrapper():
        while True:
            user_input = input("Please enter an alphabetical string: ")
            if user_input.isalpha():
                return func(user_input)
            print("Invalid input. Only alphabetical characters are allowed.")
    return wrapper

# Add more decorators here...
def require_num(func):
    @wraps(func)
    def wrapper():
        while True:
            user_input = input("Please provide a numerical string: ")
            if user_input.isdecimal():
                return func(user_input)
            print("Invalid input. Only numerical/decimal characters are allowed.")
    return wrapper
