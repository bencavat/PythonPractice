# main.py
from decorators import require_alpha, require_num

@require_alpha
def greet(name):
    print(f"Hello, {name}!")

greet()

@require_num
def ask(combination):
    print(f"Your combination is {combination}!")

ask()
