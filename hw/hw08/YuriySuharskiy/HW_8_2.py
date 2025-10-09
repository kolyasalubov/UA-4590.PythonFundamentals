import re

password = input("Enter your password: ")

def check_password(password):
    """
    This function check password for:
    1. length of password must be at least 6 characters and less than 16 characters;
    2. must contain at least one uppercase letter (A-Z);
    3. must contain at least one lowercase letter (a-z);
    4. must contain at least one digit (0-9);
    5. must contain at least one special character from the set: $#@
    """
    if len(password) < 6:
        return "Password is too short!"
    elif len(password) > 16:
        return "Password is too long!"
    elif not re.search("[a-z]", password):
        return "Password must contain a lowercase letter"
    elif not re.search("[A-Z]", password):
        return "Password must contain a uppercase letter"
    elif not re.search("[0-9]", password):
        return "Password must contain a digit"
    elif not re.search("[$#@]", password):
        return "Password must contain a special character"
    return "Your password is valid"

print(check_password(password))