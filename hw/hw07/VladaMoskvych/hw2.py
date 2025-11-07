def rectangle_area(length,width):
    """Takes the length and width of the rectangle to calculate the area"""
    area = length * width
    return area

def triangle_area(base,height):
    """Takes the base and height of the triangle to calculate the area"""
    area = 0.5 * base * height
    return area

def circle_area(radius):
    """Takes the radius of a circle to calculate the area"""
    pi = 3.14
    area = pi * radius ** 2
    return area

rectangle = 1
triangle = 2
circle = 3

choice = input("Choose a shape to calculate the area(1 - rectangle,2 - triangle, 3 - circle):")

if choice == "1":
    length = float(input("Enter the length:"))
    width = float(input("Enter the width:"))
    print(f"The area of the rectangle is {rectangle_area(length, width)}")

elif choice == "2":
    base = float(input("Enter the base:"))
    height = float(input("Enter the height:"))
    print(f"The area of the triangle is {triangle_area(base, height)}")

elif choice == "3":
    radius = float(input("Enter the radius:"))
    print(f"The area of a circle is {circle_area(radius)}")

else:
    print("Invalid choice")
