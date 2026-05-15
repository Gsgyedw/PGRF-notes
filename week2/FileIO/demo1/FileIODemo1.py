# fileIO guide

# open a file for writing
f = open("FileIODemo1.txt", "r") # other methods include 'r' for reading and 'a' for appending

test1 = f.read(5) # read the first 5 characters of the file
content1 = f.readline() # read the next line of the file
content2 = f.readlines() # read all lines of the file and return them as a list

print(test1) # print the first 5 characters
print(content1) # print the first line
print(content2) # print the content of the file as a list of lines

# write content in file
f = open("FileIODemo.txt", "a") # open the file for writing, this will overwrite the existing content
f.write("\n Goodbye World!")

f = open("FileIODemo.txt", "r") # open the file for reading
content3 = f.readlines() # read all lines of the file and return them as a list

print(content3) # print the content of the file as a list of lines

# always close the file when done
f.close() 
