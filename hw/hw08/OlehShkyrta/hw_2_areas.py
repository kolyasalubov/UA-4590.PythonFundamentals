from math import pow
from math import pi

def calc_rectangle_area(a, b):
    '''
    This function calculates the area of a rectangle 
    given the known lengths of sides a and b. 
    '''
    square_area = a * b 
    print(f'The area of a rectangle: {float(square_area)} square centimeters.')

def calc_triangle_area(a, h):
    '''
    This function calculates the area of a triangle 
    given a known side and the height drawn to that side.
    '''
    triangle_area = (1 / 2) * a * h
    print(f'The area of a triangle: {triangle_area} square centimeters.')

def calc_circle_area (r):
    '''
    This function calculates the area of a circle 
    given the known radius r. 
    '''
    circle_area = pi * pow(r, 2)
    print(f'The area of a circle: {round(circle_area,2)} square centimeters.')