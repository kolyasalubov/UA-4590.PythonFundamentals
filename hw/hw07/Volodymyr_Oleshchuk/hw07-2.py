import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

def main():
    choice = input("Choose shape (rectangle/triangle/circle): ").lower()
    if choice == "rectangle":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(area_rectangle(l, w))
    elif choice == "triangle":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(area_triangle(b, h))
    elif choice == "circle":
        r = float(input("Enter radius: "))
        print(area_circle(r))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()