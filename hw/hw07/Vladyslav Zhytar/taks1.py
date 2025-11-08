def age(age:int):
    if age<0:
        raise ValueError("Age can't be less than 0")
    return f"{age} is even" if age%2==0 else f"{age} is odd"

try:
    print(age(int(input("Enter your age: "))))
except ValueError as e:
    print(e)