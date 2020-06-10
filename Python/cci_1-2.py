#   Samuel Hulme
#   Cracking the Coding Interview
#   Question 1.2
#
#   Given two strings, wite a method to decide if one is a permutation of the other.
#
#   Thoughts:
#       1.) The simple answer is to sort the strings and then check them one letter at a time. This could be done in
#       O(nlogn) for the sort and O(n) for the comparison. Therefore, the overall runtime is O(nlogn)
#
#       2.) The quicker implementation is to use a dictionary/hashtable. Below is an example of this implementation.
#       It involves a hash table that is made up of 128 indexes where the index holds a "count" value. Each index represents
#       and ASCII character and each "count" represents the total number of times that that character has been seen in
#       String 1. We go through String 1 and add all the characters to the string. As we do this, we increase the
#       num_characters field by 1 for each new character we see. Then we go through String 2 and delete 1 from the count
#       value for each character that we see. When we hit 0, we remove one from the num_character variable. If we never
#       see a new character in String 2 and the num_characters value is 0 at the end, then the strings are permutations
#       of one another. This algorithm involves traversing each string once. Therefore the runtime is O(2n) = O(n)
#

class StringChar:
    def __init__(self, char, count):
        self.char = char
        self.count = count

    def upCount():
        self.count = self.count + 1

    def downCount():
        self.count = self.count - 1


class HashTable:
    def __init__(self):
        self.table = [None] * 128   #Assume ASCII
        self.num_characters = 0

    def determine_index(self, new_char):    #Assume ASCII
        index = ord(new_char)

    def insert_char(self, char):
        index = ord(char)
        #If already in table, add +1. If not, add the new character.
        if self.table[index] == None:   #This is a fresh index
            self.num_characters += 1
            self.table[index] = StringChar(char, 1)
        else:    #A character already exists here
            self.table[index].count += 1

    def insert_string(self, str):
        for char in str:
            self.insert_char(char)

    def compare_char_for_permutation(self, char):
        #If at a new index, count gets below 0, or num_characters gets below 0, then this is not a permutation
        index = ord(char)
        if self.table[index] == None:  # New index. This char was not in the original string
            return False
        else:  # A character already exists here
            self.table[index].count -= 1
            if self.table[index].count == 0:
                self.num_characters -= 1
                self.table[index] = None
            if self.num_characters < 0:
                return False
        return True

    def second_string_is_permutation(self, str):
        for char in str:
            if self.compare_char_for_permutation(char) == False:
                return False
        return True


def is_permutation_dict(str1, str2):
    if len(str1) != len(str2):
        return False

    hash =  HashTable()   #Init list with length twice that of the length of the strings
    hash.insert_string(str1)
    return hash.second_string_is_permutation(str2)


def is_permutation_sorted(str1, str2):
    sort_str1 = sorted(str1)    # O(nlogn)
    sort_str2 = sorted(str2)    # O(nlogn)
    if sort_str1 == sort_str2:
        return True
    return False

def check_permutations(use_dict):
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    is_perm = False
    if not use_dict:
        is_perm = is_permutation_sorted(str1, str2)
    else:
        is_perm = is_permutation_dict(str1, str2)

    print("\nThese two strings ARE permutations" if is_perm else "\nThese are NOT permutations")

#compare_str1 = "kljioilk5498u0jvc#@$%^Erlkj32ijodf$%^SDEFSeijhjel3"
#compare_str2 = "jdf$%^SDEFoil2ijo5jel3kvc#@eijhk498u0Silj$%^Erlkj3"

print("\n\nThis program will take two strings and determine if they are permutations of one another. ")
print("There are two different algorithms used to do this. Choose an algorithm from the following by entering 1 or 2.")
print("     1.) Sorting Strings First - O(nlogn)")
print("     2.) Using A Dictionary/Hash Table - O(n)")
bad_answer = True
while bad_answer:
    answer = input("Select an algorithm by typing 1 or 2: ")
    if answer == "1":
        bad_answer = False
        check_permutations(False)   #Sorting
    elif answer == "2":
        bad_answer = False
        check_permutations(True)    #Dictionary