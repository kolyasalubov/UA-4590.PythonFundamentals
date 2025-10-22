import re

def check_password(password: str) -> str:
    """
    Checks the password for compliance with security rules:
    1. Contains at least one lowercase letter (a-z)
    2. Contains at least one uppercase letter (A-Z)
    3. Contains at least one digit (0-9)
    4. Contains at least one special character ($, #, @)
    5. Has a length of at least 6 characters
    6. Has a length of no more than 25 characters
    """
    errors = [] 

    if len(re.findall(r"[a-z]", password)) == 0:
        errors.append("Password must contain at least one lowercase letter")
    if len(re.findall(r"[A-Z]", password)) == 0:
        errors.append("Password must contain at least one uppercase letter")
    if len(re.findall(r"\d", password)) == 0:
        errors.append("Password must contain at least one digit")
    if len(re.findall(r"[$#@]", password)) == 0:
        errors.append("Password must contain at least one special character ($#@)")
    if len(password) < 6:
        errors.append("Password must contain at least 6 characters")
    if len(password) > 25:
        errors.append("Password must be at most 25 characters")

    if errors:  
        return "\n".join(errors)  
    else:
        return "Password verification successful"

password = input("Enter your password: ")
print(check_password(password))