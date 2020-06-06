#   Samuel Hulme
#   Cracking the Coding Interview
#   Question 1.1
#
#   Implement an algorithm to determine if a string has all unique characters. What is you cannot use additional data structures?
#
#   Thoughts:
#   To implement this, we can use a dictionary. To do this, iterate through the list and then insert the characters into
#   a dictionary. If an element already exists for that string, we know that it is has been accessed twice.
#   Using a dictionary, which is a hashmap, we can almost always check for items in O(1), add in O(1). It will take O(n)
#   to go through the list.
#
#   contains_duplicates_dict(str)
#       Go through the string and check if the character is already in the dictionary. If so, there are duplicates. If
#       not, add to dict and continue. Using a dictionary, which is a hashmap, we can almost always check for items in
#       O(1), add in O(1). It will take O(n) to go through the list.
#
#       Pros: Quick. Runs in O(n) without lots of memory usage in the typical case.
#
#   contains_duplicates_bf(str)
#       This is the for the case where we cannot use additional data structures. In this case, we can brute force it and
#       compare each chracter to every other. This takes O(n^2).
#
#   contains_duplicates_sort(str)
#       No data structures again. This time, sort the list and then go up through it. This is O(nlogn + n) = O(nlogn)
#
#

string_with_duplicates = "Hello there young lad!"
string_no_duplicates = "abcdefg"

dup_exist = "Duplicates exist"
no_dup = "No duplicates"

def contains_duplicates_dict(str):  # O(n)
    dict = {}
    for char in str:
        if char in dict:
            return dup_exist;
        else:
            dict[char] = 1
    return no_dup

def contains_duplicates_bf(str):    # O(n^2)
    for i in range(0, len(str)):
        for j in range(i, len(str)):
            if i != j and str[i] == str[j]:
                return dup_exist
    return no_dup

def contains_duplicates_sort(str): #O(nlogn + n) = O(nlogn)
    str_sorted = ''.join(sorted(str)) #O(n) for .join()
    for i in range(1, len(str_sorted)):
        if str_sorted[i] == str_sorted[i-1]:
            return dup_exist
    return no_dup

def test_for_duplicates(type, test_string):
    if type == "D": # Dictionary
        print("  " + test_string + " >> " + contains_duplicates_dict(test_string))
    if type == "BF": # Brute Force
        print("  " + test_string + " >> " + contains_duplicates_bf(test_string))
    if type == "S": # Sorted
        print("  " + test_string + " >> " + contains_duplicates_sort(test_string))


print("\nUsing a dictionary:")
test_for_duplicates("D", string_with_duplicates)
test_for_duplicates("D", string_no_duplicates)

print("\nUsing a brute force approach:")
test_for_duplicates("BF", string_with_duplicates)
test_for_duplicates("BF", string_no_duplicates)

print("\nSorting then iterating:")
test_for_duplicates("S", string_with_duplicates)
test_for_duplicates("S", string_no_duplicates)