import re

password = input("Enter your password and we will check how secure it is: ")

pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$")
result = pattern.fullmatch(password)

if result:
    print("You have entered a strong password. Congratulations!:)")
else:
    print("You have entered a password that is too weak:(")