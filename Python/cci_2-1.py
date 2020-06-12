#   Samuel Hulme
#   Cracking the Coding Interview
#   Question 2.1
#
#   Write code to remove duplicates from an unsorted linked list. (Lets say its a singly linked list)
#
#

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def remove_next_node(self, current):
        current.next = current.next.next

    def remove_duplicates(self):
        hash = {}
        if self.head.next == None: return

        current = self.head
        while current.next != None:
            hash[current.value] = 1
            if current.next.value in hash:
                self.remove_next_node(current)
            else:
                current = current.next



    def print_list(self):
        print_string = "List: "
        current = self.head
        while current != None:
            print_string += str(current.value) + ", "
            current = current.next
        print(print_string)

def create_and_populate_linked_list(values):
    linked_list = LinkedList()
    for item in values:
        linked_list.insert_at_tail(item)
    linked_list.print_list()
    return linked_list

print("Creating List...")
linked_list = create_and_populate_linked_list([3, 3, 16, 11, 8, 14, 11, 2, 8, 16, 3, 1, 8])
linked_list.print_list()
print("Removing Duplicates...")
linked_list.remove_duplicates()
print("Duplicates Removed.")
linked_list.print_list()

print("\n\nThis program will take a list of numbers, add them to a linked list, then remove the duplicate values so that every number in the list is unique. ")
print("This implementation involves the use of a hash table, making the runtime O(n)")
num_items = input("How many numbers would you like to include in your list?: ")
values = []
for i in range(0, num_items):
    new_num = input("Enter a number: ")
    values.append(new_num)

print("Your list is: " + linked_list.print_list())
linked_list = create_and_populate_linked_list([3, 3, 16, 11, 8, 14, 11, 2, 8, 16, 3, 1, 8])
linked_list.remove_duplicates()
print("Your list without duplicates: " + linked_list.print_list())
