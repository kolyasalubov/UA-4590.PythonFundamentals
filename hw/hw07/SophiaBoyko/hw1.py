def bigger_number(arg1: int, arg2: int) -> int:
    """Function that 
    returns the largest 
    of two values"""
    if arg1 > arg2:
        return arg1
    else:
        return arg2
print(bigger_number(3, 4))