"""

Practice Problem #3
Samuel Hulme


#####################################
##           THE PROBLEM:          ##
#####################################

    Given a string, determine the length of the longest substring that does not contain any duplicate characters.

    For example:

        Given a test string "abcdedcb", the longest substring without duplicate characters would be "abcde"
        with length 5.


#####################################
##           MY SOLUTION:          ##
#####################################

    This is a sliding window problem. Therefore, it can be solved in linear time with the use of two pointers. The two
    pointers will start at the beginning of the string. One, lets call it p_fast, will move ahead of the other, p_slow.
    If p_fast sees a new character that has not yet been seen, it will add it to a dictionary of characters and then
    move ahead. This dictionary will keep record of all of the characters that have been seen so far in the substring.
    If p_fast sees a character that is already in the dictionary, we will remove the character at p_slow from the
    dictionary and move p_slow ahead one character.

#####################################
##             EXAMPLE:            ##
#####################################

    Step 1: Starting
        test_string = "abcdedcb"
             p_slow    ^
             p_fast    ^

        max_substring_length = 0
        char_seen = {}

    Step 2: Add 'a' to dictionary and move p_fast
        test_string = "abcdedcb"
             p_slow    ^
             p_fast     ^

        max_substring_length = 1
        char_seen = {'a': 1}

    Step 3-6: Add each character in "bcde" to the hash and move p_fast forward for each
        test_string = "abcdedcb"
             p_slow    ^
             p_fast         ^

        max_substring_length = 5
        char_seen = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

    Step 7: p_fast sees a duplicate character, 'd'. Therefore, remove the char at p_slow, 'a', from char_seen and move p_slow ahead one.
        test_string = "abcdedcb"
             p_slow     ^
             p_fast         ^

        max_substring_length = 5
        char_seen = {'b': 1, 'c': 1, 'd': 1, 'e': 1}

    Step 8-10: p_fast sees a duplicate character, 'd', still. Therefore, keep removing the char at p_slow and move p_slow ahead.
        test_string = "abcdedcb"
             p_slow        ^
             p_fast         ^

        substring_length = 5
        char_seen = {'e': 1}

    Step 11: Finally, the duplicate character has been removed. Now p_fast sees 'd' as a new character because it does
    not exist in char_seen. Therefore, add 'd' to char_seen and move p_fast ahead.
        test_string = "abcdedcb"
             p_slow        ^
             p_fast          ^

        substring_length = 5
        char_seen = {'e': 1, 'd': 1}

    Steps 12-....: Continue until p_fast has gone through the whole list

#####################################
##    TIME AND SPACE COMPLEXITY:   ##
#####################################

    RT = Time for p_fast to traverse list + Time for p_slow to reverse list
    RT = O(n) + O(n) where n is the length of the list
    RT = O(n)

    SC = 2 pointers + Number of characters in the longest substring
    SC = O(2) + O(N) where N is the number of characters in the longest substring
    SC = O(N)


"""


def longest_unique_substring(test_string, longest_substring=0, char_seen={}):
    p_slow = p_fast = 0
    while p_fast < len(test_string):
        if test_string[p_fast] not in char_seen:
            char_seen[test_string[p_fast]] = 1
            p_fast += 1
            longest_substring = max(longest_substring, p_fast - p_slow)
        else:
            char_seen.pop(test_string[p_slow])
            p_slow += 1
    return longest_substring


print("\nThis program will take in a string and return the length of the longest substring that does not contain")
print("duplicate characters. It uses a version of the sliding window approach to do so in O(n) time.")
input_string = input("\nPlease enter a string: ")
print("\nThe longest substring in \"" + input_string + "\" is " + str(longest_unique_substring(input_string)) + " character(s) long.")