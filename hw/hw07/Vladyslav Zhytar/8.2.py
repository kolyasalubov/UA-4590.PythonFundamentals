import re

def validation(password):
    if not (6 <= len(password) <= 16):
        return "Incorrect password"
    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_symbol = bool(re.search(r'[$#@]', password))
    
    if all([has_upper, has_lower, has_digit, has_symbol]):
        return "Nice password"
    else:
        return "Incorrect password"

password = input("Enter the password: ")

print(validation(password))
