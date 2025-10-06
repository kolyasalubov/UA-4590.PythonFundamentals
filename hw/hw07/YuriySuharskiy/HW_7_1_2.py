def circle_area():
    """
    This function calculate area of circle, based on user input
    """
    pi = 3.14
    r = int(input("Input radius of cirle: "))
    area = pi * r ** 2
    return area

def rectangle_area():
    """
    This function calculate area of rectangle, based on user inputs
    """
    a = int(input("Input length of first side of rectangle: "))
    b = int(input("Input length of second side of rectangle: "))
    area = a * b
    return area

def triangle_area():
    """
    This function calculate area of triangle, based on user inputs
    """
    b = int(input("Input length of base of triangle: "))
    h = int(input("Input length of height of rectangle: "))
    area = h * b / 2
    return area

choice = ""

while choice.lower() != "e":
    choice = input("""Choose your figure
Inputs:
c - to calculate area of circle;
r - to calculate area of rectangle;
t - to calculate area of triangle;
e - to exit
Your choose: """)
    if choice.lower() == "c":
        print(f"Area of your circle: {circle_area()}")
    elif choice.lower() == "r":
        print(f"Area of your rectangle: {rectangle_area()}")
    elif choice.lower() == "t":
        print(f"Area of your triangle: {triangle_area()}")
    elif choice.lower() == "e":
        break
    else:
        print("Type correct input or type 'e' to exit from this program!")