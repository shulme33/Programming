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
            return True
        else:
            dict[char] = 1
    return False

def contains_duplicates_bf(str):    # O(n^2)
    for i in range(0, len(str)):
        for j in range(i, len(str)):
            if i != j and str[i] == str[j]:
                return True
    return False

def contains_duplicates_sort(str): #O(nlogn + n) = O(nlogn)
    str_sorted = ''.join(sorted(str)) #O(n) for .join()
    for i in range(1, len(str_sorted)):
        if str_sorted[i] == str_sorted[i-1]:
            return True
    return False

def test_for_duplicates(type):
    test_string = input("Enter a string: ")
    duplicates_exist = False
    if type == "D": # Dictionary
        duplicates_exist = contains_duplicates_dict(test_string)
    if type == "BF": # Brute Force
        duplicates_exist = contains_duplicates_bf(test_string)
    if type == "S": # Sorted
        duplicates_exist = contains_duplicates_sort(test_string)
        
    print("\nDuplicate characters DO exist" if duplicates_exist else "\nDuplicate characters do NOT exist")
    


#print("\nUsing a dictionary:")
#test_for_duplicates("D", string_with_duplicates)
#test_for_duplicates("D", string_no_duplicates)

#print("\nUsing a brute force approach:")
#test_for_duplicates("BF", string_with_duplicates)
#test_for_duplicates("BF", string_no_duplicates)

#print("\nSorting then iterating:")
#test_for_duplicates("S", string_with_duplicates)
#test_for_duplicates("S", string_no_duplicates)

print("\n\nThis program will take a string and determine if there are duplicate characters in the string ")
print("There are three different algorithms available to do this. Choose an algorithm from the following by entering 1, 2, or 3.")
print("     1.) Using A Dictionary - O(n)")
print("     2.) Using A Brute Force Approach - O(n^2)")
print("     3.) Sorting Than Iterating - O(nlogn)")
bad_answer = True
while bad_answer:
    answer = input("\nSelect an algorithm by typing 1, 2, or 3: ")
    if answer == "1":
        bad_answer = False
        test_for_duplicates("D")   #Dictionary
    elif answer == "2":
        bad_answer = False
        test_for_duplicates("BF")    #Brute Force
    elif answer == "3":
        bad_answer = False
        test_for_duplicates("S")  #Sorting
