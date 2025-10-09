def area_rectangle(a, b):
    """
    Function for finding the area of rectangle
    """
    SR = a * b
    return (SR)

def area_triangle(base, height):
    """
    Function for finding the area of triangle
    """
    ST = 0.5 * base * height
    return (ST)

def area_circle(r):
    """
Function for finding the area of circle
    """
    SC = 3.14 * (r**2)
    return (SC)

print('Choise rectangle, triangle or circle') 
choice = str(input())
if choice == 'rectangle':
    print ('input a and b')
    a = int(input())
    b = int(input()) 
    print (area_rectangle(a,b))

elif choice == 'triangle':
    print ('input base and height')
    base = int(input())
    height = int(input()) 
    print (area_triangle(base, height))

elif choice == 'circle':
    print ('input r')
    r = int(input()) 
    print (area_circle(r))
else:
    print ('Invalid shape ')