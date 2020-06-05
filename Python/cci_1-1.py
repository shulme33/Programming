#Cracking the Coding Interview
#Question 1.1
#
#Implement an algorithm to determine if a string has all unique characters. What is you cannot use additional data structures?

#Thoughts
#To implement this, we can use a dictionary. To do this, iterate through the list and then insert the characters into
#a dictionary. If an element already exists for that string, we know that it is has been accessed twice.

def contains_duplicates_dict(str):
    dict = {}
    for char in str:
        if char in dict:
            return "Yes";
        else:
            dict[char] = 1
    return "No"

def test_for_duplicates(test_string):
    print("\nDoes \"" + test_string + "\" contain duplicate characters? >> " + contains_duplicates_dict(test_string) + "\n")

test_for_duplicates("Hello there young lad!")
test_for_duplicates("abcdefg")