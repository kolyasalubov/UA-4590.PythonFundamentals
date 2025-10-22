import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    return True

password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")