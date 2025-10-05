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
    special_characters = "$#@"
    if len(password) < 6:
        return "Password is too short!"
    if len(password) > 16:
        return "Password is too long!"
    if not any(i.islower() for i in password):
        return "Password must contain a lowercase letter"
    if not any(i.isupper() for i in password):
        return "Password must contain a uppercase letter"
    if not any(i.isdigit() for i in password):
        return "Password must contain a digit"
    if not any(i in special_characters for i in password):
        return "Password must contain a special character"
    return "Your password is valid"

print(check_password(password))