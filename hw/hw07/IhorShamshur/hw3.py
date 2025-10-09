def count_chars(text):
    """
    Function that calculates the number of characters included in a given string.
    """
    counts = {}
    
    
    for char in text:
        
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
            
    return counts

input_string = "hello"
result = count_chars(input_string)
print(result)