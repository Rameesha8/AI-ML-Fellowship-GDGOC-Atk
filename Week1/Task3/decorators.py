# decorators.py

import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper


@execution_time
def slow_function():
    total = 0
    for i in range(10_000_000):
        total += i
    print("Function completed.")


if __name__ == "__main__":
    slow_function()
