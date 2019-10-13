import sys
from collections import Counter


class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.child_left = None
        self.child_right = None


def combine_nodes(list, index1, index2):
    new_node = Node("", list[index1].freq+list[index2].freq)
    list.pop(index2)
    list.pop(index1)
    list.insert(index1, new_node)


text_to_compress = "hello there my name is samuel hulme and this is a test of the huffmans code compression algorithm"
print(len(text_to_compress))
counter = Counter(text_to_compress)         # Count up the occurrences of each letter
count_list = list(counter.items())          # Convert our data from a Counter() to a list of tuples
count_list.sort(key=lambda tup: tup[1])     # Sort the list from smallest to largest based on second value in the tuple
node_list = []                              # Empty list to hold all of our nodes

for item in count_list:
    node_list.append(Node(item[0], item[1]))


# Now we have a list of our values sorted from smallest to largest. Time to build the heap.
while len(node_list) > 1:
    combine_nodes(node_list, 0, 1)

print("Done combining")
print(node_list[0].freq)
