'''

Practice Problem 7
LRU Cache
Sam Hulme


Prompt:
    Implement an LRU cache object that can be used to get() and add() new data into the cache

What is an LRU cache?
    - An LRU cache is a cache that, when adding new data points, removes and replaces the data point which was
    references the least recently (Least Recent Used - LRU).

Thoughts:

    We will need two different data structures. First, we will want a dictionary that will count as our cache and the
    second data structure will be a linked list. Lets say that each data point we enter will consist of a key and a
    value. In that case, we can fill the cache dictionary like this:

    cache = {key1: value1}
            {key2: value2}
            {key3: value3}
            ...

    However, the values we will store will actually be references to nodes in a linked list instead of the value
    themselves. Therefore, we can change the structure to look something like the following


    cache = {key1: node1}
            {key2: node2}
            {key3: node3}
            ...

    list = <head, node3, node2, node1, tail>

    We will say that head represents the most recently referenced node and the tail points to the least recently
    referenced.

    When we go to add something, we will remove that element from the dictionary and replace it in the list. That will
    allow us to add in the new data without going over the capacity


Runtime:
    The runtime of this algorithm is constant O(1). The space complexity is negligible in the common case where the
    data we are caching is relatively large. Technically, the space complexity involves the linked list and the
    dictionary.

    RT = O(1)

    SC = dictionary + linked list = O(c) + O(c) = O(2c) where n is the capacity

'''


class CacheNode:

    def __init__(self, key, data, prev, next):
        self.data = data
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.list = []
        self.head = CacheNode("Most Recent", "", None, None)
        self.tail = CacheNode("Least Recent", "", self.head, None)
        self.head.next = self.tail
        self.capacity = capacity
        self.vacancy = capacity - 1 # Will hold how many open spots

    def write(self, key, value):
        # 1.) If not at full capacity, add
        # 2.) If at cap, find LRU
        # 3.) Remove LRU from dictionary and list
        # 4.) Add new data to dictionary and list
        if self.vacancy <= 0 and self.head.next != self.tail:
            # We want to delete from the cache and list
            lru = self.tail.prev
            self.tail.prev.next = self.tail
            self.tail.prev = lru.prev
            self.cache.pop(lru.key)
            self.vacancy += 1
        new_data = CacheNode(key, value, self.head, self.head.next)
        self.head.next.prev = new_data
        self.head.next = new_data
        self.cache[key] = new_data
        self.vacancy -= 1

    def read(self, key):
        if key not in self.cache:
            return "Data not found"
        current = self.cache[key]
        print(" -> " + current.prev.data)
        current.prev.next = current.next
        current.next.prev = current.prev
        current.prev = self.head
        current.next = self.head.next
        self.head.next = current
        return current.data

    def print_lru(self):
        print("\n")
        current = self.head

        while current is not None:
            print(str(current.key) + " -- " + str(current.data))
            current = current.next
        print("\n")

lru = LRUCache(4)
#lru.write("a", "Data A")
#lru.write("b", "Data B")
#lru.write("c", "Data C")
#lru.write("d", "Data D")
#lru.write("e", "Data E")
#lru.write("f", "Data F")
#lru.write("g", "Data G")
#lru.write("h", "Data H")
#lru.write("i", "Data I")

#lru.print_lru()


#print("\nRead \"e\":" + lru.read("e"))
#lru.print_lru()

print("This program implements an LRU cache. From the list below, select either to read"
      "of write data to and from the cache. Then, based on your answer and subsequent"
      "data entry, the cache will be printed and will show the most recently and least"
      "recently referenced data.")

user_selection = ""
while user_selection != "quit":
    print("    r: Read data from the cache"
        "\n    w: Write data to the cache"
          "quit: Quit program")
    user_selection = input("Choose from the options above: ")
    if user_selection == "r":
        print("    Read")
    elif user_selection == "w":
        print("    Write")
        new_data = input("Enter data to add to the cache: ")
        new_key = input("Enter a unique key for this data: ")
        lru.write(new_key, new_data)
        lru.print_lru()
    elif user_selection == "quit":
        continue;
    else:
        print("\n\"" + user_selection + "\" is not a valid choice. Please choose again.")
