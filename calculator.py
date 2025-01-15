def binary_to_decimal(binary_str):
    decimal = 0
    for counter, char in enumerate(binary_str[::-1]): # Makes the binary string in reverse order
        if char != '1' and char != '0': # If character is not 1 or 0 it returns "Error"
            return 'Error'
        if char == '1': # If the characetr is 1, it calculates its value based on the position
            decimal += 2 ** counter
    return decimal


def binary_calculator(bin1, bin2, operator):
    num1 = binary_to_decimal(bin1)
    num2 = binary_to_decimal(bin2)
   
    if num1 == 'Error' or num2 == 'Error':
        return 'Error'
   
    
    # Perfroms the operation based on the givern operator
    if operator == '/':
        if num2 == 0: # Checks for divsion by 0 and returns "Nan" if it is
            return 'NaN'
        else:
            total = num1 / num2
    elif operator == '+':
        total = num1 + num2
    elif operator == '-':
        total = num1 - num2
    elif operator == '*':
        total = num1 * num2
    
    # Checks if the result is outside the 8 bit digit rang (0-255)
    if total > 255 or total < 0:
        return 'Overflow'
    
    # Converts the results back to 8 bit binary
    output = ''
    num_bits = total.bit_length()
    for i in range(num_bits -1, -1, -1): # Starts from the highest bit and goes down to 2^0
        power = 2 ** i
        if total >= power: # Checks if the current power of 2 fits into the total
            output += '1' 
            total -= power
        else:
            output += '0'

    return output



