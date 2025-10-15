import random
from random import randint

def guess_the_number():
    secret_number = randint(1, 100)
    MAX_TRIES = 10
    guessed_correctly = False

    print("--------------------------------------------------")
    print("        Welcome to the 'Guess the Number' Game      ")
    print("--------------------------------------------------")
    print(f"You have {MAX_TRIES} attempts to guess it.")

    for attempt in range(1, MAX_TRIES + 1):
        guess_input = input(f"\nAttempt {attempt}/{MAX_TRIES}. Enter your guess: ")
        guess = int(guess_input)

        if guess < secret_number:
            print("My number is GREATER than yours. Try again!")
        elif guess > secret_number:
            print("My number is LESS than yours. Try again!")
        else:
            guessed_correctly = True
            print(f"\nCongratulations! You guessed the number!")
            break

    if not guessed_correctly:
        print("\n==================================================")
        print(" Game over.")
        print("==================================================")

if __name__ == "__main__":
    guess_the_number()