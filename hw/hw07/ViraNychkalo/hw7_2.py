# Завдання 2
# Напишіть програму, яка обчислює площу прямокутника, трикутника та кола 
# (напишіть три окремі функції для обчислення площі.
#   Викликайте їх у головній програмі залежно від вибору користувача).
def find_rectanglearea(width, height):
    return width*height
    

def find_trianglearea(base, heightt):
    return (base*heightt)/2
    

def find_circlearea(radius):
    PI = 3.12
    return PI*(radius**2)


choice = int(input("Що ви хочете обчислити? Площу квадрата - 1, площу трикутника - введіть 2, площу кола - введіть 3:"))
if choice == 1:
    width = int(input("Введіть ширину:"))
    height = int(input("Введіть висоту:"))
    print("Площа квадрата:", find_rectanglearea(width,height))

elif choice == 2:
    base = int(input("Введіть основу трикутника: "))
    heightt = int(input("Введіть висоту: "))
    print("Площа трикутника:", find_trianglearea(base, heightt))

elif choice == 3:
    radius = int(input("Введіть радіус: "))
    print("Площа кола:", find_circlearea(radius))

else:
    print("Такого варіанту немає.")