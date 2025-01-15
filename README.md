[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17649562)
# Binary Calculator
 This is a simple Python program that performs basic arithmetic operations on two binary numbers. It takes two binary numbers as strings, an operator (ex. +, -, *, /), and returns the result as an 8 bit binary number. It also handles errors for invalid inputs and out of range results.

# Features

Converts binary numbers to decimal.

Supports basic operations: addition (+), subtraction (-), multiplication (*), and division (/).

Converts the result back to an 8-bit binary string.

Handles errors like invalid binary input, division by zero, and out-of-range results.

# How to Use

1. Function

The function binary_calculator takes three arguments:

bin1: First binary number as a string (ex.`1010`).

bin2: Second binary number as a string (ex.`0110`).

operator: Arithmetic operator (`+`, `-`, `*`, `/`).

2. Example Usage

result = binary_calculator(`1010`, `1010`, `+`)
print(result)  # Output: `00010100` (20 in decimal)

3. Error Handling

Invalid binary input (ex.`1020`) returns `Error`.

Division by zero returns `NaN`.

Results outside the 8-bit range return `Overflow`.