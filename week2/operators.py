# arithmetic operators:

## addition operator (+):
print(5 + 3) # output will be 8 (adds 5 and 3)

## subtraction operator (-):
print(5 - 3) # output will be 2 (subtracts 3 from 5)

## multiplication operator (*):
print(5 * 3) # output will be 15 (multiplies 5 and 3)

## division operator (/):
print(5 / 3) # output will be 1.666666666666666

## floor division operator (//):
print(5 // 3) # output will be 1 (finds the quotient of the division of 5 by 3)

## modulus operator (%):
print(5 % 3) # output will be 2 (finds the remainder of the division of 5 by 3)

## exponentiation operator (**):
print(2 ** 3) # output will be 8 (raises 2 to the power of 3)   

# simultananeous assignment:
a, b, c = 1, 2, 3
a, b, c = 1 * 2, 2 * 3, 3 * 4
print(a, b, c) # output will be 2 6 12 (assigns the results of the expressions to a, b, and c respectively)

# relational operators:
print(5 > 3) # output will be True (checks if 5 is greater than 3)
print(5 < 3) # output will be False (checks if 5 is less than 3)
print(5 >= 3) # output will be True (checks if 5 is greater than or equal to 3)
print(5 <= 3) # output will be False (checks if 5 is less than or equal to 3)
print(5 == 3) # output will be False (checks if 5 is equal to 3)
print(5 != 3) # output will be True (checks if 5 is not equal to 3)

# logical operators:
print(True and False) # output will be False (returns True if both operands are true)
print(True or False) # output will be True (returns True if at least one operand is true)
print(not True) # output will be False (returns the opposite of the operand)

# type conversion:
print(int(3.5)) # output will be 3 (converts the float 3.5 to an integer by truncating the decimal part)
print(float(3)) # output will be 3.0 (converts the integer 3 to a float by adding a decimal point)
print(str(3.5)) # output will be '3.5' (converts the float 3.5 to a string)
print(bool(0)) # output will be False (converts the integer 0 to a boolean, which is False)