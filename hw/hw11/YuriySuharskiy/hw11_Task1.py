class NegativeAgeError(Exception):
    def __init__(self,data):
        self.data = data


def check_age(age):
    try:
        age = int(age)
        if age < 0:
            raise NegativeAgeError("Your input is negative")
        if age % 2 == 0:
            return "Your age is even"
        else:
            return "Your age is odd"
    except ValueError:
        return "Incorrect input"
    except NegativeAgeError as e:
        return str(e)

age = input("Input your age: ")
print(check_age(age))
