def binary_calculator(bin1, bin2, operator):
    num1 = 0
    total = 0
    # Converts the first binary string to its decimal number 
    for counter, char in enumerate(bin1[::-1]): # Makes the binary string in reverse order
        if char != '1' and char != '0': # If character is not 1 or 0 it returns "Error"
            return 'Error'
        if char == '1': # If the characetr is 1, it calculates its value based on the position
            num1 += 2 ** counter
   
    # Same as first process just for the second binary string
    num2 = 0
    for counter, char in enumerate(bin2[::-1]):
        if char != '1' and char != '0':
            return 'Error'
        if char == '1':
            num2 += 2 ** counter
    
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
    powers = [128, 64, 32, 16, 8, 4, 2, 1]

    output = ''
    for power in powers:
        if total >= power: # Checks if the current power of 2 fits into the remaning value
            output += '1' 
            total -= power
        else:
            output += '0'

    return output

    

print(binary_calculator("1010", "1010", "+"))  # Should return "10100"
print(binary_calculator("1100", "0011", "-"))  # Should return "1001"
print(binary_calculator("1010", "0000", "/"))  # Should return "NaN"
print(binary_calculator("1010", "abc", "+"))   # Should return "Error"


