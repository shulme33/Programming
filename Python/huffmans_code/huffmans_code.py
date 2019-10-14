import sys
from collections import Counter


class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.child_left = None
        self.child_right = None


def combine_nodes(node_list, index1, index2):
    new_node = Node("", node_list[index1].freq + node_list[index2].freq)
    new_node.child_left = node_list[index1]
    new_node.child_right = node_list[index2]
    node_list.pop(index2)
    node_list.pop(index1)

    if len(node_list) == 0:
        node_list.append(new_node)
    else:
        for i in range(0, len(node_list)):
            if i == len(node_list)-1 and node_list[i].freq <= new_node.freq:
                node_list.append(new_node)
                break
            elif node_list[i].freq > new_node.freq:
                node_list.insert(i, new_node)
                break


def encode(text):
    encoded_binary_local = ""
    for letter in text:
        encoded_binary_local += encoding[letter]
    return encoded_binary_local


def get_encoded_values(node, current_code):
    if node.value != "":  # Leaf Node
        print(node.value, " >> ", current_code)
        encoding[node.value] = current_code
    else:
        get_encoded_values(node.child_left, current_code+"0")
        get_encoded_values(node.child_right, current_code+"1")


text_to_compress = "hello there everyone how are you doing? it is good to see everyone and I hope that you are all well"
counter = Counter(text_to_compress)         # Count up the occurrences of each letter
count_list = list(counter.items())          # Convert our data from a Counter() to a list of tuples
count_list.sort(key=lambda tup: tup[1])     # Sort the list from smallest to largest based on second value in the tuple
node_list = []                              # Empty list to hold all of our nodes

for item in count_list:
    node_list.append(Node(item[0], item[1]))

# Now we have a list of our values sorted from smallest to largest. Time to build the heap.
while len(node_list) > 1:
    combine_nodes(node_list, 0, 1)

print("\nMin Heap Created. \nEncoding to Binary...")
encoding = {}
get_encoded_values(node_list[0], "")    # Recursive function to find all new encoded binary values
encoded_binary = encode(text_to_compress)
print("\nEncoding Complete.")
print(encoded_binary)
