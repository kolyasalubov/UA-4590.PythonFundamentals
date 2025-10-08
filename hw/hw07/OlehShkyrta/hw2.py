import math

prefered_calc = int(input('''Hello, please tell me what shape area you want to calculate? \n
Enter 1 for a rectangle, 2 for a triangle, and 3 for a circle. '''))

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
    circle_area = math.pi * r ** 2
    print(f'The area of a circle: {round(circle_area,2)} square centimeters.')

if prefered_calc == 1:
    print("Great! You have selected the rectangle shape. Now you need to enter the parameters for calculation.")
    side_a = int(input("Please enter the length of side a: "))
    side_b = int(input("Please enter the length of side b: "))
    calc_rectangle_area(side_a, side_b)
elif prefered_calc == 2:
    print("Great! You have selected the triangle shape. Now you need to enter the parameters for calculation.")
    side_a = int(input("Please enter the length of side a: "))
    height = int(input("Please enter the length of height: "))
    calc_triangle_area(side_a, height)
elif prefered_calc == 3:
    print("Great! You have selected the circle shape. Now you need to enter the parameters for calculation.")
    radius = int(input("Please enter the radius of the circle r: "))
    calc_circle_area(radius)
else:
    print("You have entered an incorrect value. To enter a new value, run the program again.")