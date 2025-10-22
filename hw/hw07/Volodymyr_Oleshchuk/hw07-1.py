def find_largest(a, b):
    """
    Returns the largest of two numbers.
    """
    return a if a > b else b

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(find_largest(a, b))