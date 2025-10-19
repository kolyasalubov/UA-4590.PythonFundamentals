def day_id(id):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    try:
        id = int(id)
    except ValueError:
        return "Id must be an integer"
    if id > 7:
        return "Id can't be larger than 7"
    if id <= 0:
        return "Id can't be less then 1"
    return days[id-1]


run = 0
while run == 0:
    id = input("Input id (or 'exit' to leave):")
    if id.lower() == 'exit':
        run = 1
    else:
        print(f"Your day is {day_id(id)}")
    
