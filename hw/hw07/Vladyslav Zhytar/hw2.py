from math import sqrt,pi

def area_of_rectangle(height,width):
    '''
    Calculate area of rectangle
    '''
    return height*width

def area_of_triangle(side1,side2,side3):
    '''
    Calculate area of triangle
    '''
    p=(side1+side2+side3)/2
    return sqrt(p*(p-side1)*(p-side2)*(p-side3))

def area_of_circle(radius):
    '''
    Calculate area of circle
    '''
    return pi*radius**2

def menu():
    """
    the function responsible for the mini-menu
    """
    print("Choose the option: ",end="\n")
    print("1-Rectangle", "2-Triangle", "3-Circle",sep="\n" )
    number=int(input("Choose: "))
    if number==1:
        height=float(input("Enter the height: "))
        width=float(input("Enter the width: "))
        print(area_of_rectangle(height,width))
    elif number==2:
        side1=float(input("Enter the first side: "))
        side2=float(input("Enter the second side: "))
        side3=float(input("Enter the third side: "))
        print(area_of_triangle(side1,side2,side3))
    elif number==3:
        radius=float(input("Enter the radius: "))
        print(area_of_circle(radius))

menu()