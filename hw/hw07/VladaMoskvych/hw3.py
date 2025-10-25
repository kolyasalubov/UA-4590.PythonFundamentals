def character_number(word):
    """Calculates the number of characters in a word"""
    result = dict()
    for x in word:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result

print(character_number("Vlada"))