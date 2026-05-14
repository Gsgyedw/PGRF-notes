# sequence structure (if ... else ... elif):

## multiple if ... else statements:

x = 10
# selects or ignores action. If condition True, below code will run (under if)
if x > 0:
    print("x is positive") # output will be "x is positive" (because x is greater than 0)
# if condition False, below code will run (under elif)
elif x == 0:
    print("x is zero") # this code will be ignored (because x is greater than 0)
# if condition False, below code will run (under else)
else:
    print("x is negative") # this code will be ignored (because x is greater than 0)

# nested if ... else statements:
y = 5
if y > 0:
    if y < 10:# output will be "y is a positive single-digit number" (because y is greater than 0 and less than 10)
        print("y is a positive single-digit number") 
    else: # this code will be ignored (because y is less than 10)
        print("y is a positive number with multiple digits") 
else: # this code will be ignored (because y is greater than 0)
    print("y is not a positive number") 
