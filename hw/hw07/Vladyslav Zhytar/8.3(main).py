import find_area as f

area=input("Enter the area of the figure you are looking for: ")

if area=="Rectangle":
    print(f.area_rectangle(float(input("Enter first side: ")),float(input("Enter second side: "))))
elif area=="Triangle":
    print(f.area_triangle(float(input("Enter height: ")),float(input("Enter side: "))))
elif area=="Circle":
    print(f.area_circle(float(input("Enter radius: "))))
else:
    print("Incorrect figure name")