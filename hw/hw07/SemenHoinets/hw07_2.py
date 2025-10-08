#Define useful functions that calculates areas for different figures
def rectangle_area(length, width):
    """
    Return value of a rectangle area.
    """
    return length * width


def triangle_area(base, height):
    """
    Return value of a triangle area.
    """
    return base * height * 0.5


def circle_area(radius):
    """
    Return value of a circle area.
    """
    PI = 3.14
    return PI * radius ** 2


#Ask user for specific shape
shape_type = input("Area to be calculated(rectangle/triangle/circle): ").lower().strip()

#Prints the result for a user acording to case handling
match shape_type:
    case "rectangle":
        length = int(input("Length: "))
        width = int(input("Width: "))

        print(f"Area of this {shape_type} equal: {rectangle_area(length, width)}")
    case "triangle":
        base = int(input("Base: "))
        height = int(input("Height: "))

        print(f"Area of this {shape_type} equal: {triangle_area(base, height)}")
    case "circle":
        radius = int(input("Radius: "))

        print(f"Area of this {shape_type} equal: {circle_area(radius)}")
    case _:
        print(f"Wrong shape type! '{shape_type.capitalize()}' area isn't provided.")

