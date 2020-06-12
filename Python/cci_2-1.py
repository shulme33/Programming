#   Samuel Hulme
#   Cracking the Coding Interview
#   Question 2.1
#
#   Write code to remove duplicates from an unsorted linked list. (Lets say its a singly linked list)
#
#   The Algorithm:
#       Go through the list once. As we go, if we have not seen the number before, add it to a hash table/dictionary.
#       If we have seen it, delete the node that contains it. This algorithm's runtime is O(n).

import sys

##################################################
##              Individual Nodes                ##
##################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

##################################################
##               The Linked List                ##
##################################################

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, value):    #Insert a new node at the end of the linked list
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def remove_next_node(self, current):    #Remove a node from the list
        current.next = current.next.next

    def remove_duplicates(self):    #Remove all redundant nodes from the list
        hash = {}
        if self.head.next == None: return

        current = self.head
        while current.next != None:
            hash[current.value] = 1
            if current.next.value in hash:
                self.remove_next_node(current)
            else:
                current = current.next

    def print_list(self):   #Print out the list in a nice format
        print_string = "["
        current = self.head
        while current != None:
            print_string += str(current.value) + ", "
            current = current.next
        print_string = print_string[:-2] + "]"
        return print_string


##################################################
##              Public Functions                ##
##################################################

def create_and_populate_linked_list(values):    #Create the linked list
    linked_list = LinkedList()
    for item in values:
        linked_list.insert_at_tail(item)
    linked_list.print_list()
    return linked_list

def get_number_between(low, high, prompt):  #Get valid input. A number between "low" and "high".
    num_items = low
    while num_items <= low or num_items > high:
        try:
            num_items = int(input(prompt))
        except:
            num_items = low
    return num_items

##################################################
##   Get input values to build the linked list  ##
##################################################

print("\nThis program will take a list of numbers, add them to a linked list, then ")
print("remove the duplicate values so that every number in the list is unique. ")
print("This implementation involves the use of a hash table, making the runtime O(n)")
num_items = get_number_between(0, 100, "\nHow many numbers, between 1 and 100, would you like to include in your list?: ")
values = []
for i in range(0, num_items):
    new_num = get_number_between(-10000, 10000, "Enter a number between +-10,000: ")
    values.append(new_num)

#################################################
##   Create linked list and remove duplicates  ##
#################################################

linked_list = create_and_populate_linked_list(values)
print("\nYour list is: " + linked_list.print_list())
linked_list.remove_duplicates()
print("Your list without duplicates: " + linked_list.print_list() + "\n")
