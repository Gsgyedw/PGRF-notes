# sequence structure (if ... else):

## single if ... else statement:
x = 10
# selects or ignores action. If condition True, below code will run (under if)
if x > 0: 
    print("x is positive") # output will be "x is positive" (because x is greater than 0)
# if condition False, below code will run (under else)
else:
    print("x is not positive") # this code will be ignored (because x is greater than 0)

# operators for conditions:
# comparison operators:

# greater than operator:
if x > 5: # output will be True (checks if x is greater than 5)
    print("x is greater than 5")

# less than operator:
if x < 15: # output will be True (checks if x is less than 15)
    print("x is less than 15")

# greater than or equal to operator:
if x >= 10: # output will be True (checks if x is greater than or equal to 10)
    print("x is greater than or equal to 10")

# less than or equal to operator:
if x <= 20: # output will be True (checks if x is less than or equal to 20)
    print("x is less than or equal to 20")

# equal operator:
if x == 10: # output will be True (checks if x is equal to 10)
    print("x is equal to 10")

# not equal operator:
if x != 0: # output will be True (checks if x is not equal to 0)
    print("x is not equal to 0")