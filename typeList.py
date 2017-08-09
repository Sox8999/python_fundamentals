"""
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
Copy
# input
l = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"
Copy
# input
l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"
"""

mix_list = ['magical unicorns ',19,'hello ',98.98,'world']
int_list = [99,5,12,25,30,16,9]
str_list = ['I am ','a little teapot ','short and stout']

def list_type(lst):
    new_str = ''
    total = 0

    for item in lst:
        if isinstance(item, int) or isinstance(item, float):
            total += item
        elif isinstance(item, str):
            new_str += item

    if new_str and total:
        print "The array you entered is of mixed type"
        print "String:", new_str
        print "Sum:", total

    elif new_str:
        print "The array you entered is of string type"
        print "String:", new_str

    else:
        print "The array you entered is of a number type"
        print "Sum:", total

print list_type(mix_list)
print list_type(int_list)
print list_type(str_list)

            

