# utils.py

def greet_user(name):
    return f"Hello, {name}! Welcome back."


def calculate_average(*args):
    """Accepts any number of values"""
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


def display_info(**kwargs):
    """Displays key-value info"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


square = lambda x: x * x
