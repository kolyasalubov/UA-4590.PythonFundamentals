numbers = (43,28)

def return_large_number(num1, num2):
    '''
    This function return the large number
    ''' 
    return max(num1, num2)

large_number = return_large_number(*numbers)
print(large_number)
