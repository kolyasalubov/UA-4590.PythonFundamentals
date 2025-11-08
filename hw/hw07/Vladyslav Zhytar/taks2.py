def what_day(number):
    if not isinstance(number,int) or number>7 or number<1:
        raise ValueError("Number must be int type and less than 8") 
    
    match number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        
try:
    print(what_day(int(input("Enter the number: "))))
except ValueError as e:
    print(e)