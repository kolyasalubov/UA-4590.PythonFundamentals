def count_characters(text: str) -> dict:
    """Calculate and return a 
    dictionary with the number 
    of occurrences of each 
    character in the given string."""
    dict_1 = {}
    for char in text:
        if char not in dict_1:
            dict_1[char] = 1
        else:
            dict_1[char] += 1
    return dict_1

text = input().replace('"', '')
print(count_characters(text))