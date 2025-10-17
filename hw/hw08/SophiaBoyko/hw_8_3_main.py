from math import pow, pi as PI
from hw_8_3_module import rectangle_area, triangle_area, circle_area

choice = input("Enter the shape to calculate area (rectangle, triangle, circle): ")

if choice == "rectangle":
    params = ["length", "width"]
    values = []
    for param in params:
        value = float(input(f"Enter the following value {param}: "))
        values.append(value)
    print("Area of rectangle =", rectangle_area(*values))
elif choice == "triangle":
    params = ["base", "height"]
    values = []
    for param in params:
        value = float(input(f"Enter the following value {param}: "))
        values.append(value)
    print("Area of triangle =", triangle_area(*values))
else:
    params = ["radius"]
    values = []
    for param in params:
        value = float(input(f"Enter the following value {param}: "))
        values.append(value)
    print("Area of circle =", circle_area(*values, PI))