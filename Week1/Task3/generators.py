# generators.py

# Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# Custom Range Generator
def custom_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step


if __name__ == "__main__":
    print("Fibonacci Sequence:")
    for num in fibonacci(10):
        print(num, end=" ")

    print("\nCustom Range:")
    for num in custom_range(1, 10, 2):
        print(num, end=" ")
