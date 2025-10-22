import pygame
from random import randint

random_number = randint(1, 101)

print("""Welcome to the Number Guessing Game!
You have 10 attempts to guess a number between 1 and 100.""")

for attempt in range(1,11):
    input_number = int(input(f"Attemp {attempt}. Enter the number: "))
    if input_number < random_number:
          print("The guessed number is greater!")
    elif input_number > random_number:
          print("The guessed number is less!")
    else:
        print(f"Congratulations! You guessed the number {random_number} in {attempt} attempts!")
        break
else:
    print(f"Attempts exhausted! The guessed number was {random_number}.")
