"""

Practice Problem #2
Samuel Hulme


#####################################
##           THE PROBLEM:          ##
#####################################

    You have a 2D grid representing a
    rectangular lake with water
    denoted as 'o' and land denoted
    as 'x':

    [
        [o,o,o,o,o,x,o,o,o,o],
        [o,o,x,o,x,x,o,o,o,o],
        [o,o,x,x,o,o,o,o,o,o],
        [o,o,o,x,x,o,o,o,o,o],
        [x,o,x,x,x,o,o,o,x,x],
        [o,o,x,x,x,o,x,o,o,x],
        [o,o,o,o,o,o,x,o,o,o],
        [o,o,o,o,o,o,x,o,o,o],
        [x,x,x,x,o,o,o,o,o,o],
        [x,o,o,o,o,o,o,o,o,o],
    ]

    Assume the lake is surrounded by land.

    Mark all of the land that is not connected
    to the surrounding land as 'i' for island.

    Connections can only occur if the space
    is adjacent to the up, down, right, and
    left directions. (diagonal does not
    count)

    e.g.:

    [
        [o,o,o,o,o,x,o,o,o,o],
        [o,o,i,o,x,x,o,o,o,o],
        [o,o,i,i,o,o,o,o,o,o],
        [o,o,o,i,i,o,o,o,o,o],
        [x,o,i,i,i,o,o,o,x,x],
        [o,o,i,i,i,o,i,o,o,x],
        [o,o,o,o,o,o,i,o,o,o],
        [o,o,o,o,o,o,i,o,o,o],
        [x,x,x,x,o,o,o,o,o,o],
        [x,o,o,o,o,o,o,o,o,o],
    ]

#####################################
##           MY SOLUTION:          ##
#####################################

    This problem can best be solved through a DFS. First, we will loop through each location on the lake. If it is
    an 'x', then we start a DFS where we will look at all of its neighbors and then continue recursively if that
    neighbor is another 'x'. If not, then leave it alone. While we are doing this, we will be replacing the 'x'
    with an integer value that will represent the particular island that we are looking at. At the end, every
    island will have its own distinct integer character to represent it. While searching, we will be adding the
    island locations to a dictionary. This dictionary will have keys that are the island number and the values will
    be the list of locations that correspond to that island number. The only special case is that the first spot
    in the list of locations will actually be a single character that will represent whether or not that island is
    a peninsula. At the end of searching through the list, we will loop through the islands and set all of the
    different indexes to their appropriate values.

#####################################
##             EXAMPLE:            ##
#####################################

    example_lake = [
        [o, o, o, o, x, o, o]
        [o, o, x, o, x, x, o]
        [o, o, x, o, o, o, o]
        [x, o, o, o, x, o, o]
        [o, o, x, x, x, o, x]
        [o, o, o, o, o, o, x]
    ]

    hash_of_islands = {}

    After the DFS and looping has finished, we will have the following

    example_lake = [
        [o, o, o, o, 0, o, o]
        [o, o, 1, o, 0, x, o]
        [o, o, 1, o, o, o, o]
        [2, o, o, o, 3, o, o]
        [o, o, 3, 3, 3, o, 4]
        [o, o, o, o, o, o, 4]
    ]

    hash_of_islands = {
        0: ['x', (4, 0), (4, 1)]
        1: ['i', (2, 1), (2, 2)]
        2: ['x', (0, 3)]
        3: ['i', (3, 4), (4, 4), (4, 3), (4, 2)]
        4: ['x', (6, 4), (6, 5)]
    }

    After this point, we will loop through the different islands that are listed in hash_of_islands and will set the
    indexes to the value in the 0 spot of the list. For example, Island #0 will set the two points (4,0) and (4,1)
    to the letter 'x', signifying that it is a peninsula. Island #1 will set the two points (2,1) and (2,2) to the
    letter 'i', signifying that it is an island. After this, all the islands will be set to 'i' and the peninsulas
    will be set to 'x'.

#####################################
##    TIME AND SPACE COMPLEXITY:   ##
#####################################

    RT = Initial look + DFS + Resetting values

    RT = O(n) + O(n) + O(i) where n is the number of locations and i is the number of locations that are islands
    In the worst case, all but the edges are island locations, in which case i = n-2w-2h+4 where w is the width and
    h is the height of the lake. in that case the runtime simplifies to

    RT = O(3n-2w-2h+4)
    RT = O(n)

    Space Complexity - Not including original lake

    SC = Hash + DFS
    SC = O(I) + O(N) where I = number of islands + peninsulas and N = Number of locations in the largest island

"""


def print_lake(lake):
    for row in lake:
        print_row = ""
        for item in row:
            print_row += "{:<3}".format(item)
        print(print_row)


def set_as_island(lake, r, c, islands, counter):
    if c < 0 or c >= len(lake[0]) or r < 0 or r >= len(lake):     # This spot is not on the board
        islands[counter][0] = 'x'
        return
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # Right, top, bottom, left
    if lake[r][c] == 'x':
        islands[counter].append((r, c))
        lake[r][c] = str(counter)
        for dir in directions:
            set_as_island(lake, r+dir[0], c+dir[1], islands, counter)


def switch_to_island(lake, islands={}, x=0, y=0):
    counter = 0
    for r, row in enumerate(lake):
        for c, spot in enumerate(row):
            if lake[r][c] == 'x':   # First time seeing an island
                islands[counter] = ['i']
                set_as_island(lake, r, c, islands, counter)
                counter += 1
    counter -= 1
    while counter >= 0:
        new_value = islands[counter][0]
        del islands[counter][0]
        for location in islands[counter]:
            lake[location[0]][location[1]] = new_value
        counter -= 1
    return lake


lake_initial = [
    ['o', 'o', 'o', 'o', 'o', 'x', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'x', 'o', 'x', 'x', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'x', 'x', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'x', 'x', 'o', 'x', 'o', 'o', 'o'],
    ['x', 'o', 'x', 'x', 'x', 'o', 'x', 'o', 'x', 'x'],
    ['o', 'o', 'x', 'x', 'x', 'o', 'x', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'x', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'x', 'o', 'o', 'o'],
    ['x', 'x', 'x', 'x', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
]

print("\nThis program will take a 2D list, meant to represent a lake, and replace all of the island locations with \"i\"")
print("Shown below is the lake. Every \"o\" represents water and every \"x\" represents land")
print("Is a group of x's touch the edge at any point, they are considered to be a peninsula. Else, they are an island.")
print("This program will replace all islands with the letter \"i\" and leave all peninsulas with the letter \"x\"")
print("\nThe initial lake:\n")
print_lake(lake_initial)
print("\n\nAfter replacement:\n")
print_lake(switch_to_island(lake_initial))


