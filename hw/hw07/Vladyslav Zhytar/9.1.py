from random import randint as ri

win_number=ri(1,100)
tries=0

user_number=None

win=user_number==win_number

while not win and tries<10:
    user_number=int(input("Enter the number: "))
    if user_number>win_number:
        print("The number is less!")
    elif user_number==win_number:
        win=True
        break
    else:
        print("The number is more!")
    tries+=1
    print(f'{tries}', "tries left")
if win:
    print("-----------[WIN!]-----------")

if tries>=10:
    print("----------------[FAIL!]------------------")
    print("You don't have more tries")