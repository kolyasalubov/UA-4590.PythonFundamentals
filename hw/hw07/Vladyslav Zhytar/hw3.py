def calculate_the_number_of_characters(message):
    my_dict={}
    for item in message:
        if item in my_dict:
            continue
        my_dict[item]=message.count(item)
    return my_dict

message=(input("Enter the message: "))
print(calculate_the_number_of_characters(message))
