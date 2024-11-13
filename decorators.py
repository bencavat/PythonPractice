# decorators.py
"""
Decorator practice file.
"""
from functools import wraps
import time

# require_alpha input decorator function that loops until someone provides an aphabetical string
def require_alpha(func):
    @wraps(func)
    def wrapper():
        while True:
            user_input = input("Please enter an alphabetical string: ")
            if user_input.isalpha():
                return func(user_input)
            print("Invalid input. Only alphabetical characters are allowed.")
    return wrapper

# require_num input decorator function that loops until someone provides a num
def require_num(func):
    @wraps(func)
    def wrapper():
        while True:
            user_input = input("Please provide a numerical string: ")
            if user_input.isdecimal():
                return func(user_input)
            print("Invalid input. Only numerical/decimal characters are allowed.")
    return wrapper

# Decorator to time a function
def timer(func):
    """A decorator that prints the runtime of the decorated function."""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)
        end_time = time.time()  # End time
        run_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {run_time:.4f} seconds")
        return result
    return wrapper_timer
