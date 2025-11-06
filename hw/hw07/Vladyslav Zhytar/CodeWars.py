#7.1
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

#7.2
# from math import dist
# def distance(x1, y1, x2, y2):
#     p=(x1,y1)
#     q=(x2,y2)
#     return round(dist(p,q),2)

#7.3
# def filter_words(st):
#     st=st.capitalize()
#     my_list=st.split()
#     stt=" ".join(my_list)
#     return stt

#7.4
# def number_to_string(num):
#     return str(num)

#7.5
# def reverse(st):
#     return " ".join(reversed(st.split())).strip()

#7.6
# def reverse_list(l):
#     return l[::-1]

#7.7
# def solution(number):
#     my_list=[]
#     for item in range(number):
#         if item<0:
#             return 0
#         elif item%3==0 or item%5==0:
#             my_list.append(item)
#     return sum(my_list)

#7.8
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return True if mpg*fuel_left>=distance_to_pump else False

#7.9
# def are_you_playing_banjo(name):
#     return f'{name} plays banjo' if name.lower().startswith("r") else f'{name} does not play banjo'

#7.10
# def bool_to_word(boolean):
#     return "Yes" if boolean is True else "No"

#7.11
# def count_sheeps(sheep):
#     return sheep.count(True)

#7.12
# def correct_tail(body, tail):
#      return True if body[-1]==tail else False