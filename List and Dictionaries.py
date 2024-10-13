'''
List in Python
'''
name = ["John", "Matthew", "Peter", "Nicole", "Princess", "Victoria"]
my_list = [1, 3, 7.77, 2, 35, 53, 77 ,89, 101, 1001]
num_elmts = len(my_list)
print(num_elmts)

#list methods

my_list.append(55) #Adds element to the endpoint of the list
print(my_list)

my_list.insert(4, 15)  # Inserts element at a chosen index in the list insert(index, element)
print(my_list)

my_list.extend([2, 557,83,9])
print(my_list)

print(my_list.count(2)) #Counts how many times an element repeats itself in the list

print(name.index("Nicole"))

name.reverse() #Reverses the list
print(name)

my_list.sort() #Arrange the list in ascending order
print(my_list)

print(my_list.__add__(name)) #Adds a list of items to another list



"""
Dictionareis in Python
"""

my_data = {"name": "Samuel", "age": "25", "height":"1.69 m"}  #Dictionary takes the key and value {"key": "value"}
print(my_data.keys())

print(list(my_data.keys()))

my_data["location"],my_data[ "occupation"]= "Accra", "Full Stack WebDev"  #This is how to append data in dictionary
print(my_data)

author_1 = {"name": "Al Sweigart"}
author_2 = {"name": "Robert De Marco"}

my_authors = [author_1,author_2]
print(my_authors)
