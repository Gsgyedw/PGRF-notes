# few methods for string formatting:
name = "Alice" 
age = 30
# using the % operator:
print("My name is %s and I am %d years old." % (name, age))
# using the .format() method: (reccommended, this is best practice)
print("My name is {} and I am {} years old.".format(name, age)) 
# using f-strings (available in Python 3.6+):
print(f"My name is {name} and I am {age} years old.") 
# all will output: My name is Alice and I am 30 years old.

# formatting options: 
# :d for integers, 
# :f for floating-point numbers (will expose 6 DP regardless, unless specifed otherwise), 
# :.2f for 2 decimal places):

whole_number = 42
floating_number = 3.14159
print(f"Whole number: {whole_number:d}")  # output: Whole number: 42
print(f"Floating-point number: {whole_number:f}")  # output: Floating-point number: 42.000000
print(f"Floating-point number (4 decimal places): {whole_number:.4f}")  # output: Floating-point number (4 decimal places): 42.0000
print(f"Floating-point number (2 decimal places): {floating_number:.2f}")  # output: Floating-point number (2 decimal places): 3.14

# padding and aligning strings:
print('<{:>10}>'.format("Hello"))  # right-align with width of 10
print('<{:<10}>'.format("Hello"))  # left-align with width of 10
print('<{:^10}>'.format("Hello"))  # center-align with width of 10

#character padding:
print('<{:*>10}>'.format("Hello"))  # right-align with width of 10, using '*' as padding character
print('<{:*<10}>'.format("Hello"))  # left-align with width of 10, using '*' as padding character
print('<{:*^10}>'.format("Hello"))  # center-align with width of 10, using '*' as padding character

# str formatting applications (using f string):
name = "Bob"
age = 25
year = 1
average_score = 88.56789

print(f"{'Name':7}{'Age':5}{'Year':5}{'Average Score':15}")
print(f"{name:7}{age:<5}{year:<5}{average_score:^10.2f}")

# output will be:
# Name   Age  Year Average Score  
# Bob    25   1      88.57 