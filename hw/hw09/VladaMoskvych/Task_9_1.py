import random
from random import randint

secret_number = randint(1,100)

for x in range(10):
    user_input = int(input(f" You have {10-x} tries left. Enter your guess: "))

    if user_input == secret_number:
        print("Congratulations! Right guess.")
        break
    elif user_input < secret_number:
        print("Too low. Try again.")
    elif user_input > secret_number:
        print("Too high. Try again.")
    
else:
    print("You've run out of tries. Game over")






