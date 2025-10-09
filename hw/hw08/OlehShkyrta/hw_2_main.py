import hw_2_areas

prefered_calc = int(input('''Hello, please tell me what shape area you want to calculate? \n
Enter 1 for a rectangle, 2 for a triangle, and 3 for a circle. '''))

if prefered_calc == 1:
    print("Great! You have selected the rectangle shape. Now you need to enter the parameters for calculation.")
    side_a = int(input("Please enter the length of side a: "))
    side_b = int(input("Please enter the length of side b: "))
    hw_2_areas.calc_rectangle_area(side_a, side_b)
elif prefered_calc == 2:
    print("Great! You have selected the triangle shape. Now you need to enter the parameters for calculation.")
    side_a = int(input("Please enter the length of side a: "))
    height = int(input("Please enter the length of height: "))
    hw_2_areas.calc_triangle_area(side_a, height)
elif prefered_calc == 3:
    print("Great! You have selected the circle shape. Now you need to enter the parameters for calculation.")
    radius = int(input("Please enter the radius of the circle r: "))
    hw_2_areas.calc_circle_area(radius)
else:
    print("You have entered an incorrect value. To enter a new value, run the program again.")