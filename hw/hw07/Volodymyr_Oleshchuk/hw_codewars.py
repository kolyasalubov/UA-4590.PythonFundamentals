#1
def greet(name):
    if name == "Johny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


#2
import math
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


#3
def filter_words(st):
    st = st.split(" ")
    modified_sentence = ""
    for item in st:
        if item != "":
            modified_sentence += (item + " ")
        else:
            continue
    return modified_sentence.capitalize().strip()


#4
def number_to_string(num):
    return str(num)


#5
def reverse(st):
    st = st.split(" ")[::-1]
    new_str = ""
    for item in st:
        new_str += item + " "
    return new_str.strip()


#6
def reverse_list(l):
    return l[::-1]


#7
def solution(number):
    if number < 0:
        return 0
    result = 0
    for item in range(1, number):
        if item % 3 == 0 or item % 5 == 0:
            result += item
    return result 


#8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg < distance_to_pump:
        return False
    return True


#9
def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return (name + " plays banjo") 
    return (name + " does not play banjo")


#10
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    return "No"


#11
def count_sheeps(sheep):
    counter = 0
    for item in sheep:
        if item == True:
            counter += 1
    return counter


#12
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False