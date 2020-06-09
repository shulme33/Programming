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
#       2.) The quicker implementation is to use a dictionary/hashtable. For each string add the different characters
#       to the dictionary. For the first, you will just be adding them. For the second, we will be checking to see
#       if the chracter in question is already in the dictionary. Each time we insert into the string during the inital add,
#       we will update each entry to show the number of letters of that type that we have seen so far. For example, if
#       we are comparing the string "abbcccdddd" to the string "ddddcccbba", then we will initially add the first string
#       to the dictionary and will save the frequency of that chracter. The dictionry will contain 4 entries (a:1), (b:2),
#       (c:3), (d:4). Then when we add entries from the second string, we will count down these values. Each time we add
#       a "d" from the second string, we will count the (d:4) tuble down by one, i.e. (d:3)...(d:2). Once a tuple hits a count
#       of 0, we will remove it from a count of overall characters seen in the first string. That way, we know how many
#       different characters still have unmatched entries as we go through the 2nd string
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

    def print_hash(self):
        for i in self.table:
            if i == None:
                print("None")
            else:
                print(i.char + " >> " + str(i.count))

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

    def compare_string_for_permutation(self, str):
        for char in str:
            if self.compare_char_for_permutation(char) == False:
                return False
        return True


def is_permutation_dict(str1, str2):
    not_perm = "Not Permutation"
    is_perm = "Is Permutation"
    if len(str1) != len(str2):
        return not_perm

    hash =  HashTable()   #Init list with length twice that of the length of the strings
    hash.insert_string(str1)
    print(hash.num_characters)
    is_permutation = hash.compare_string_for_permutation(str2)
    if is_permutation:
        return is_perm
    else:
        return not_perm



def is_permutation_sorted(str1, str2):
    sort_str1 = sorted(str1)    # O(nlogn)
    sort_str2 = sorted(str2)    # O(nlogn)
    if sort_str1 == sort_str2:
        return "Is Permutation"
    return "Not Permutation"

def check_permutations(str1, str2, alg):
    if alg == "Sort":
        print("   Sorted Algorithm: " + is_permutation_sorted(str1, str2))
    elif alg == "Dict":
        print("   Dictionary Alg: " + is_permutation_dict(str1, str2))

compare_str1 = "abbccccdddd"
compare_str2 = "abcdbcdcdd"
print("\nComparing " + compare_str1 + " >> " + compare_str2)
check_permutations(compare_str1, compare_str2, "Dict")
print("\n")