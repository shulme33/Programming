"""

Practice Problem #4
Samuel Hulme


#####################################
##           THE PROBLEM:          ##
#####################################

    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
    sequence from beginWord to endWord, such that:
        1.) Only one letter can be changed at a time.
        2.) Each transformed word must exist in the word list.

    Note:
        1.) Return 0 if there is no such transformation sequence.
        2.) All words have the same length.
        3.) All words contain only lowercase alphabetic characters.
        4.) You may assume no duplicates in the word list.
        5.) You may assume beginWord and endWord are non-empty and are not the same.

    Example 1:

        Input:

        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

        Output: 5

        Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
        return its length 5.

    Example 2:

        Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]

        Output: 0

        Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

#####################################
##           MY SOLUTION:          ##
#####################################

    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

            hit                 O(1)
         /   |   \
    *it     h*t     hi*         O(26n)  -> n = length of string
   /  \     /  \    |   \
**t  *i*  **t  h**  h**  *i*    O(26^2n)


    This is a problem that can be solved through the use of BFS. We will think about this like a tree. At the root is
    the beginWord. Then, we will go through the different characters of beginWord and loop through all 26 letters
    of the alphabet to see if any exist in the set. If they do, add it to the queue and remove that item from the set.

        beginWord = "run"
        endWord = "car"

        We will have "run" at the root and will check the dictionary for the words  "aun", "bun", "cun", "dun" and so on.

    After we have put all of the values on the queue, we will check for iterations of those words and so on and so on...

    At the end, the number of necessary changes will be the depth of the tree. The most it can be is the length of the
    beginWord. That could happen in the case where every character in beginWord needs to change.



#####################################
##             EXAMPLE:            ##
#####################################

    For the example, lets say that the dictionary contains all possible words.

    beginWord = "run"
    endWord = "car"

    In the example below, a * represents a character from the endWord and a % represents a character from the level above

    Our tree will look like:

                   run
               /    |    \
        *un        r*n         ru*
         |          |           |
        **n        r**         *u*

#####################################
##    TIME AND SPACE COMPLEXITY:   ##
#####################################

    RUNTIME:

    The runtime is a combination of the time to look at the different iterations of the word and the time to traverse
    the tree. In the worst case, we will add every node in the dictionary to the tree. Lets call that number of nodes N.
    The second part is going through each of the letters in the words. Lets say the words are of length M.

    Therefore, the runtime is O(MN)

    SPACE COMPLEXITY:

    Lets say we have N words in the dictionary of length M.

    SC = O(MN)

"""
