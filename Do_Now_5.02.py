'''
############
Do Now 5.02
############

1. In your Console
------------------
Type the following:

my_dictionary = {
'kittens': 'cute animals'
}
my_dictionary['kittens'] = 'p. cute'
print(my_dictionary)

In your Notebook
----------------
Respond to the following:

Write down what the 2nd line does.
This replaces the value of kittens with 'p. cute'

2. In your Console
------------------
my_dictionary = {}
my_dictionary['puppies'] = 'baby dogs'
print(my_dictionary)

Continue in your Notebook
-------------------------
Respond to the following prompt
Write down what the 2nd line does.
This line adds the key 'puppies' and adds the value 'baby dogs' to it

3. In your Console
my_dictionary = {
'kittens': 'cute animals',
'puppies': 'baby dogs'
}

my_dictionary.pop('kittens')
print(my_dictionary)
my_dictionary.pop('bunnies')
my_dictionary.pop('bunnies', None)

Continue In your Notebook
Write down what the second line does.
This line removes kittens from the dictionary

What is different between my_dictionary.pop('bunnies') and my_dictionary.pop('bunnies', None)?
The latter just returns nothing if a key is absent from a dictionary, the former will give an error if a key is absent
'''
# step 1
my_dictionary = {
'kittens': 'cute animals'
}
print(my_dictionary)
my_dictionary['kittens'] = 'p. cute'
print(my_dictionary)

# step 2
my_dictionary = {}
my_dictionary['puppies'] = 'baby dogs'
print(my_dictionary)

# step 3
my_dictionary = {
'kittens': 'cute animals',
'puppies': 'baby dogs'
}
my_dictionary.pop('kittens')
print(my_dictionary)
my_dictionary.pop('bunnies')
my_dictionary.pop('bunnies', None)