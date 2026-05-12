# valid way to create a string:

print(type('Hello, World!'))
print(type("Hello, World!"))
print(type('''Hello, World!'''))
print(type("""Hello, World!"""))

# output will indicate that all of the above are of type 'str'
# triple quotes can be used to create multi-line strings:
message = """Welcome
to the world of Python!"""
print(message)

# concatenation of strings (use the + operator):
# must have str value as operand, otherwise will raise a TypeError
# cant concatenate str and int
height = 1.79
print("My height is " + str(height) + " meters.")

# keyword arg - end:
# defines what to print at the end of the output, default is newline character (\n)
print("Hello", end=";")
print("World")

# output will be: Hello;World!

#keyword arg - sep:
#defines own separator between multiple values in print function, default is space
print("Hello", "World", sep="!!")

#output will be: Hello!!World

#escape sequences:
#use backslash (\) to include special characters in a string
print("She said, \"Hello!\"")  # includes double quotes in the string

# output will be: 
# She said, "Hello!"

#use \n for new line and \t for tab:
print("Line 1\nLine 2") # output will be: 
# Line 1
# Line 2
print("Column 1\tColumn 2") # output will be: Column 1    Column 2