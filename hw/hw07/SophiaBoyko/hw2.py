def rectangle_area(length: float, width: float) -> float:
    """Calculate and return 
    the area of a rectangle."""
    area = round(length * width, 2)
    return area

def triangle_area(base: float, height: float) -> float:
    """Calculate and return 
    the area of a triangle."""
    area = round(1/2 * base * height, 2)
    return area

def circle_area(radius: float) -> float:
    """Calculate and return 
    the area of a circle."""
    PI = 3.14
    area = round(PI * (radius**2), 2)
    return area

choice = input("Enter the shape to calculate area (rectangle, triangle, circle): ")

if choice == "rectangle":
    params = ["length", "width"]
    values = []
    for param in params:
        value = float(input(f"Enter the following value {param}: "))
        values.append(value)
    print("Area of triangle =", rectangle_area(*values))
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
    print("Area of circle =", circle_area(*values))