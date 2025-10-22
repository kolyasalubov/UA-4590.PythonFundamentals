### --- Task 2 ---
"""
Write a program that calculates the area of a rectangle, triangle and circle
(write three functions to calculate the area, and call them in the
main program depending on the user's choice).
"""

def calc_area(figure):
    
    if figure.lower() not in ("rectangle", "triangle", "circle"):
        print("Error, figure type is incorect.")
        figure = input("Enter the type of a figure (only rectangle, triangle, circle): ")
        return calc_area(figure)


    elif figure.lower() == "rectangle":

        def clac_rectangle(arg1, arg2):
            rectangle_area = arg1 * arg2
            return rectangle_area

        side_1 = float(input("Enter the length of the first side: "))
        side_2 = float(input("Enter the length of the second side: "))
        print(clac_rectangle(side_1, side_2))
    
    elif figure.lower() == "triangle":

        def calc_triangle(a, h):
            triangle_area = 1/2 * a * h
            return triangle_area

        side_a = float(input("Enter the length of the 'a' side: "))
        height = float(input("Enter the length of the height: "))
        print(calc_triangle(side_a, height))

    elif figure.lower() == "circle":

        def calc_circle(r):
            pi = 3.14
            circle_area = pi * r**2
            return circle_area

        radius = float(input("Enter the length of the radius: "))
        print(calc_circle(radius))

figure = input("Enter the type of a figure (Only rectangle, triangle and circle is allowed): ")
calc_area(figure)