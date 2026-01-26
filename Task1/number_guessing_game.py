import random

secret_number = random.randint(1, 10)
guess = 0

print("Guess the number between 1 and 10")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")
