# lists:

"""a list is a collection of items that are ordered and changeable. 
Lists are defined using square brackets [] and can contain items of different data types."""

# creating a list:
my_list = [1, 2, 3, "Hello", True]
print(my_list) # output will be [1, 2, 3, 'Hello', True]

# can also create a empty list and add items later:
empty_list = []

# nested lists:
nested_list = [1, 2, [3, 4], "Hello"]

# to access items in a list:
print(my_list[0]) # output will be 1 (indexing starts at 0

# negative indexing:
print(my_list[-1]) # output will be True (last item)

# to access part of items in a nested list:
print(nested_list[1:3]) # output will be [2, [3, 4]] (accesses items from index 1 to 2)
print(nested_list[3:]) # output will be ['Hello'] (accesses the string 'Hello' in the nested list)
print(nested_list[:2]) # output will be [1, 2] (accesses the first two items in the nested list)
print(nested_list[2:4]) # output will be [[3, 4], 'Hello'] (accesses items from index 2 to 3)

# operators for lists:
# concatenation operator (+):
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2) # output will be [1, 2, 3, 4, 5, 6] (combines the two lists)

# in operator:
print(2 in list1) # output will be True (checks if 2 is an item in list1)
print(4 in list1) # output will be False (checks if 4 is an item in list1)

# == operator:
print(list1 == list2) # output will be False (checks if list1 and list2 are equal, which means they have the same items in the same order)

# != operator:
print(list1 != list2) # output will be True (checks if list1 and list2 are not equal)

# functions for lists:
# getting the length of a list:
print(len(my_list)) # output will be 5 (number of items in the list)

# find smallest item in a list:
numbers = [5, 2, 9, 1, 5]
print(min(numbers)) # output will be 1 (smallest item in the list)

# find largest item in a list:
print(max(numbers)) # output will be 9 (largest item in the list)

# more built-in functions for lists:
# adding an item to the end of the list using .append():
my_list.append("World")
print(my_list) # output will be [1, 2, 3, 'Hello', True, 'World']

# extending a list with another list using .extend():
my_list.extend([4, 5])
print(my_list) # output will be [1, 2, 3, 'Hello', True, 'World', 4, 5]

# inserting an item at a specific index using .insert():
list1 = [1, 2, 3]
list1.insert(1, "Inserted")
print(list1) # output will be [1, 'Inserted', 2, 3] (inserts 'Inserted' at index 1)

# removing an item from the list using .remove():
list1.remove("Inserted")
print(list1) # output will be [1, 2, 3] (removes the first occurrence of 'Inserted' from the list)

# removing an item at a specific index using .pop():
popped_item = list1.pop(1)
print(popped_item) # output will be 2 (removes and returns the item at index 1)
print(list1) # output will be [1, 3] (list after popping the item at index 1)

# finding the index of an item using .index():
print(my_list.index("Hello")) # output will be 3 (index of the first occurrence of 'Hello' in the list)

# list the number of occurrences of an item using .count():
print(my_list.count("Hello")) # output will be 1 (number of times 'Hello' appears in the list)

# reversing the list using .reverse():
my_list.reverse()
print(my_list) # output will be [5, 4, 'World', True, 'Hello', 3, 2, 1] (reverses the order of the items in the list)

# sorting the list using .sort():
numbers = [5, 2, 9, 1, 5]
numbers.sort()
print(numbers) # output will be [1, 2, 5, 5, 9] (sorts the items in the list in ascending order)

# clearing all items from the list using .clear():
my_list.clear()
print(my_list) # output will be [] (removes all items from the list, resulting in an empty list)