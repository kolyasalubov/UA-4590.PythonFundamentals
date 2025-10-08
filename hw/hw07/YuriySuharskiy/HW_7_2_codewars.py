#I

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    
print(greet("Johnny"))

#II

def distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
    return round(distance, 2)

#III

def filter_words(st):   
    filtered_string = " ".join(st.split()).capitalize()
    return filtered_string

#IV

def number_to_string(num):
    return str(num)

#V

def reverse(st):
    st = " ".join(st.split()[::-1])
    return st

#VI

def reverse_list(l):
    return l[::-1]

#VII

def solution(number):
    num_list = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            num_list.append(i)

    return sum(num_list)

#VIII

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

#IX

def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
#X

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"

#XI

def count_sheeps(sheep):
    return sheep.count(True)
    
#XII

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    return False