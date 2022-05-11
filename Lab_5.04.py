'''
############
# Lab 5.04 #
############
In this lab we will use our word-counting code from Lab 5.02 to create a program that 
determines the top 5 most commonly used words in a passage of text. After processing 
the passage, it prints the top 5 words and the number of times each occurs.

Here's one strategy for completing this lab:

Repackage some of your code from Lab 5.02 to make two functions: 
text_to_word_list(), that  takes a single passage of text and splits into a list of words; 
and count_frequencies(), that takes in a list of words and returns a dictionary of word 
frequencies

Write a new function, find_max_valued_key(), that takes a dictionary as an argument, and 
returns the key that is associated with the largest value in that dictionary. Internally, 
this function loops through the dictionary while keeping track of the largest value it's 
seen so far and the key that goes along with that value.

Run find_max_valued_key() once on the dictionary of word counts, print out the key/value 
of word it returns.

Remove that key from the dictionary.

Repeat steps 3-4 four more times: Call find_max_valued_key(), print out the key/value pair, 
and remove the key.

If there is a tie within find_max_valued_key(), choose among the tied items however you like 
and return just one of them.

Example
--------
Here's an example of the program output with the text passage set to the opening lines of Dr. 
Seuss's poem Green Eggs and Ham:

I am Sam. I am Sam. Sam-I-am.

That Sam-I-am! That Sam-I-am!
I do not like that Sam-I-am!

Would you like green eggs and ham?

I do not like them, Sam-I-am.
I do not like green eggs and ham.

Would you like them here or there?

I would not like them here or there.
I would not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.

Would you like them in a house?
Would you like them with a mouse?

I do not like them in a house.
I do not like them with a mouse.
I do not like them here or there.
I do not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.
>>> python3 most_frequent_words.py
i, 22
like, 17
not, 13
do, 11
them, 12

Bonus
----------
The process of finding the largest element, printing it, and removing it from the dictionary 
is a way to sort items. Write a function that will return a sorted list of all the words from 
most frequent to least frequent.

Change the code to find the least frequent words.
'''
# variables
paragraph = '''
I am Sam. I am Sam. Sam-I-am. 

That Sam-I-am! That Sam-I-am! 
I do not like that Sam-I-am! 

Would you like green eggs and ham? 

I do not like them, Sam-I-am. 
I do not like green eggs and ham. 

Would you like them here or there? 

I would not like them here or there. 
I would not like them anywhere. 
I do not like green eggs and ham. 
I do not like them, Sam-I-am. 

Would you like them in a house? 
Would you like them with a mouse? 

I do not like them in a house. 
I do not like them with a mouse. 
I do not like them here or there. 
I do not like them anywhere. 
I do not like green eggs and ham. 
I do not like them, Sam-I-am.
'''

word_count_dict = {}

# functions
def text_to_word_list():
    global paragraph
    paragraph_lower = paragraph.lower()
    paragraph_lower_no_punctuation = paragraph_lower.replace(".", "")
    paragraph_lower_no_punctuation = paragraph_lower_no_punctuation.replace("\n", "")
    paragraph_lower_no_punctuation = paragraph_lower_no_punctuation.replace("?", "")
    paragraph_lower_no_punctuation = paragraph_lower_no_punctuation.replace("!", "")
    word_list = paragraph_lower_no_punctuation.split(" ")
    return word_list

def count_frequencies():
    global word_count_dict
    for word in text_to_word_list():
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    print(word_count_dict)

def find_max_valued_key(dictionary):
    max_key = max(dictionary, key = dictionary.get)
    max_value = max(dictionary.values())
    print(f"{max_key}: {max_value}")
    dictionary.pop(max_key, max_value)
    print(f"{max_key}: {max_value}")


count_frequencies()
find_max_valued_key(word_count_dict)