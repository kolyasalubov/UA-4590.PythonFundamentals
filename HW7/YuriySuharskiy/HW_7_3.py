def num_of_characters(user_string):
    """
    This function calculate number of characters in given string
    """
    result = {}
    check_string = user_string.lower().replace(" ","")
    for letter in check_string:
        result[letter] = check_string.count(letter)
    return result
