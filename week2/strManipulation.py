# to access character in a string:
text = "Hello, World!"
print(text[1]) # output will be 'e' (indexing starts at 0)

# negative indexing:
print(text[-1]) # output will be '!' (last character)
print(text[-2]) # output will be 'd' (second last character)

# string slicing:
print(text[0:5]) # output will be 'Hello' (slices from index 0 to 4, end index is exclusive)

# if start index is omitted, it defaults to 0; if end index is omitted, it defaults to the length of the string
print(text[7:]) # output will be 'World!' (slices from index 7 to the end of the string)
print(text[:5]) # output will be 'Hello' (slices from the beginning to index 4)

# str operators:

# concatenation operator (+):
greeting = "Hello"
print(greeting + " World!") # output will be 'Hello World!'

# repetition operator (*):
print("Hello " * 3) # output will be 'Hello Hello Hello '

# membership operator (in):
print("World" in text) # output will be True (checks if 'World' is a substring of text)
print("Python" in text) # output will be False (checks if 'Python' is a substring of text)  

# membership operator (not in):
print("Python" not in text) # output will be True (checks if 'Python' is not a substring of text)
print("World" not in text) # output will be False (checks if 'World' is not a substring of text)

# getting the length of a string:
print(len(text)) # output will be 13 (number of characters in the string, including spaces and punctuation)

# str functions:

# capitalize the first character of the string:
print(text.capitalize()) # output will be 'Hello, world!' (only the first character is capitalized, the rest are lowercase)

# converting to uppercase:
print(text.upper()) # output will be 'HELLO, WORLD!'

# coverting to lowercase:
caps = "HELLO, WORLD!"
print(caps.lower()) # output will be 'hello, world!'

# finding the index of a substring:
print(text.find("World")) # output will be 7 (index of the first occurrence of 'World' in the string)
print(text.find("Python")) # output will be -1 (indicates that 'Python' is not found in the string)
## finds the substring 'lo' starting from index 0 to 4:
print(text.find("lo", 0, 5))  # output will be 3 (finds 'lo' in the substring 'Hello', which is from index 0 to 4)

# replacing a substring with another substring:
print(text.replace("World", "Python")) # output will be 'Hello, Python!' (replaces 'World' with 'Python' in the string)
print(text.replace("World", "Python", 3)) 
# output will be 'Hello, Python!' (replaces 'World' with 'Python' in the string, but only the first 3 occurrences)

# check for only alphanumeric characters:
alphanumeric = "Hello"
print(alphanumeric.isalpha()) # output will be True (checks if all characters in the string are alphanumeric (letters only))

# check if str contains only digits:
numeric = "12345"
print(numeric.isdigit()) # output will be True (checks if all characters in the string are digits)

# splits the string into a list of substrings based on a specified delimiter (default is whitespace):
csv = "apple,banana,cherry"
csv_list = csv.split(",") # splits the string at each comma to make a list
print(csv_list) # output will be ['apple', 'banana', 'cherry'] (a list of substrings)