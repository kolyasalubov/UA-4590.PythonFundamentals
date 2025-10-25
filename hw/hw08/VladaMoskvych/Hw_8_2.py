import re

"""Checks the password for compliance with security rules: 
1. Contains at least one lowercase and one uppercase letter (a-z)
3. Contains at least one digit (0-9) 
4. Contains at least one special character ($, #, @) 
5. Has a length between 6 and 16 characters"""

valid = False

while not valid:
    password = input("Please enter the password here:")

    if (
        len(password) >=6 and len(password)<=16 
        and re.search(r"[a-z]", password) 
        and re.search(r"[A-Z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[$#@]", password)
    ):
        valid = True
        print("Thank you. Your password complies to the rules")

    else:
        print("Your password does not comply to the rules. Please try again.") 