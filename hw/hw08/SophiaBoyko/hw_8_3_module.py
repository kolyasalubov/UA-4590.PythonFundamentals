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

def circle_area(radius: float, PI) -> float:
    """Calculate and return 
    the area of a circle."""
    area = round(PI * (pow(radius, 2)), 2)
    return area
