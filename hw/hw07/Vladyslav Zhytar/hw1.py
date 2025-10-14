def choose_bigger_number(num1,num2):
    """
    The function returns a larger number
    """
    if num1>num2:
        return num1
    return num2

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print(choose_bigger_number(num1,num2))