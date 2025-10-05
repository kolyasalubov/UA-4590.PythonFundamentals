from math import pi, pow
from HW_8_3_module import circle_area, rectangle_area, triangle_area


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
        print(f"Area of your circle: {circle_area(pi, pow)}")
    elif choice.lower() == "r":
        print(f"Area of your rectangle: {rectangle_area()}")
    elif choice.lower() == "t":
        print(f"Area of your triangle: {triangle_area()}")
    elif choice.lower() == "e":
        break
    else:
        print("Type correct input or type 'e' to exit from this program!")  