### --- Task 1 ---
"""
Write a function that returns the largest number of two numbers
(use DocStrings documentation strings in the function).
"""

def my_func(num1, num2):
    """
    Return the largest of two numbers.

    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The larger of the two numbers.
    """
    return max(num1, num2)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(my_func(num1, num2))
