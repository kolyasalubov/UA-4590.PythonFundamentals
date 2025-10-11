import random

number = random.randint(1, 100)
guess = None
attempts = 0

print("""Welcome to the Number Guessing Game!
You have 10 attempts to guess a number between 1 and 100.""")
while guess != number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1
    if attempts > 10:
        print(f"Sorry, you've used all your attempts. The number was {number}.")
        break
    print(f"Attempt {attempts}/10")
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")