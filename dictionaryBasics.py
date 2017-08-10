"""
Assignment: Making and Reading from Dictionaries
Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

Write a function that will print something like the following as it executes:

My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python
Copy
There are two steps to this process, building a dictionary and then gathering all the data from it. Write a function that can take in and print out any dictionary keys and values.

Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. Repeat this assignment a few times to really get the hang of 
unpacking dictionaries, as it's a very common requirement of any web application.
"""

info = { "name": "Bryse", "age": 28, "country": "USA", "language": "Javascript"} 

def output(x):
    print "My name is ",x["name"]
    print "My age is ",x["age"]
    print "My country of birth is the ",x["country"]
    print "My favorite language is ",x["language"]

output(info)
