'''Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

Here's an example:

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
Copy
Hint: how many loops will you need to complete this task?
'''

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def find_char(lst):
    new_lst = []

    for text in lst:
        if char in text:
            new_lst.append(text)
    print new_lst
    

find_char(word_list)