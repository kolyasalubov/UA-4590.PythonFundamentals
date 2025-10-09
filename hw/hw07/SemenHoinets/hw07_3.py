def number_of_characters(str):
    """
    Return dict with number of charecters included in given string in (character, number) pairs
    """
    
    return {char: str.count(char) for char in str}


