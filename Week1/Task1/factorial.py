number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)
4