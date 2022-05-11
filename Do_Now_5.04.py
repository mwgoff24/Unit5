'''
###############
# Do Now 5.04 #
###############

1. In your Console
------------------
Type the following:
my_dictionary = {
'a': 1,
'b': 2,
'c': 3,
'd': 4,
'e': 5
}
print(list(my_dictionary))

In your Notebook
----------------
Respond to the following:
Write down what list() does when given a dictionary.
Takes the keys and makes them items in a list.

What type does list() return?
List

Write down how you might use a for loop to go through and print the values of my_dictionary.
for item in my_dictionary:
    print(my_dictionary[item])

2. In your Console
------------------
Challenge yourself
Try your solution to 3.
'''
my_dictionary = {
'a': 1,
'b': 2,
'c': 3,
'd': 4,
'e': 5
}
print(type(list(my_dictionary)))