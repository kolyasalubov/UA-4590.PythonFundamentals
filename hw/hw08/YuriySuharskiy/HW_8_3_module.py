def circle_area(pi, func):
    """
    This function calculate area of circle, based on user input
    """
    r = int(input("Input radius of cirle: "))
    area = pi * func(r,2)
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
    area = 0.5 * h * b
    return area