import sys
from collections import Counter


class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.child_left = None
        self.child_right = None


def combine_nodes(node_list, index1, index2):   # Collapse list into heap
    new_node = Node("", node_list[index1].freq + node_list[index2].freq)
    new_node.child_left = node_list[index1]     # Set child 1
    new_node.child_right = node_list[index2]    # Set child 2
    node_list.pop(index2)
    node_list.pop(index1)

    if len(node_list) == 0:                     # If we are down to the last node
        node_list.append(new_node)
    else:
        for i in range(0, len(node_list)):      # Determine where to re-add composite node
            if i == len(node_list)-1 and node_list[i].freq <= new_node.freq:
                node_list.append(new_node)      # Add to end of list
                break
            elif node_list[i].freq > new_node.freq:
                node_list.insert(i, new_node)   # Add somewhere in the middle of list
                break


def encode(text):   # Encode text to binary
    encoded_binary_local = ""
    for letter in text:
        encoded_binary_local += encoding[letter]
    return encoded_binary_local


def decode(binary_text, root):  # Decode binary back into raw text
    current_node = root
    current_binary = 0  # Current bit in binary string
    decoded_text = ""

    while current_binary <= len(binary_text):
        decoded_text += current_node.value
        if current_binary == len(binary_text):
            break
        current_node = root if current_node.value != "" else current_node   # Move back to root if new letter just added
        current_node = current_node.child_left if binary_text[current_binary] == "0" else current_node.child_right
        current_binary += 1
    return decoded_text


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

for item in count_list:                     # Create list of nodes
    node_list.append(Node(item[0], item[1]))

while len(node_list) > 1:                   # Build Min Heap
    combine_nodes(node_list, 0, 1)

print("\nMin Heap Created. \nEncoding to Binary...")
encoding = {}                               # Dictionary for encoded values
get_encoded_values(node_list[0], "")        # Recursive algorithm to find encoded values
encoded_binary = encode(text_to_compress)   # Get binary equivalent

print("\nEncoded Binary:")
print(encoded_binary)                       # Encode text to binary

print("\nDecoded Text:")
print(decode(encoded_binary, node_list[0])) # Decode our binary
