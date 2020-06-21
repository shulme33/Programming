"""

Mark the Lake Islands:

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

##########################
##      Solutions       ##
##########################

Runtime: O(wh)
Space: O(log(wh))
Space (Sam): O(i) + O(I) -> i = # islands I=size of the largest land mass

[o,o,o,o,o,1,o],
[o,o,4,o,x,x,o],
[o,o,4,4,o,o,o],
[o,o,o,4,4,o,o],
[3,o,4,4,4,o,2],
[o,o,o,o,o,o,2],

[0,0,0,0,0,1,0]
[0,0,4,0,1,1,0]
[ , , , ,0,0, ]
[ , , , , , , ]
[ , , , , , , ]
[ , , , , , , ]

[1, "x"]
[2, "x"]
[3, "x"]
[4, "i"]

width = w
height = h

Runtime - O(wh) + O(wh) + O((w-2)(h-2)) -> O(wh)
Space - O(2wh)

O(wh + wh + wh - 2h - 2w + 4)
O(3wh - 2w - 2h + 4)
O(wh - w - h)
O(wh)



"""

lake = [
        ['o','o','o','o','o','x','o','o','o','o'],
        ['o','o','x','o','x','x','o','o','o','o'],
        ['o','o','x','x','o','o','o','o','o','o'],
        ['o','o','o','x','x','o','o','o','o','o'],
        ['x','o','x','x','x','o','o','o','x','x'],
        ['o','o','x','x','x','o','x','o','o','x'],
        ['o','o','o','o','o','o','x','o','o','o'],
        ['o','o','o','o','o','o','x','o','o','o'],
        ['x','x','x','x','o','o','o','o','o','o'],
        ['x','o','o','o','o','o','o','o','o','o'],
]

peninsulas = []

def print_lake():
    for row in lake:
        print(row)

def check_top(x, y):
    if y == 0: return [-1, -1]
    else: return [x, y-1]

def check_left(x, y):
    if x == 0: return [-1, -1]
    else: return [x-1, y]

def check_right(x, y):
    if x == len(lake[0]): return [-1, -1]
    else: return [x+1, y]

def check_bottom(x, y):
    if y == len(lake): return [-1, -1]
    else: return [x, y+1]

def is_symbol(x, y, symbol):
    if y >= 0 and x >= 0 and y < len(lake) and x < len(lake[0]) and lake[x][y] == symbol:
        return True
    return False


def check_surroundings(x, y, island_num, check_val):
    #Top
    top_x, top_y = check_top(x, y)
    if is_symbol(top_x, top_y, check_val):
        lake[top_x][top_y] = island_num
        check_surroundings(top_x, top_y, island_num, check_val)

    #Right
    right_x, right_y = check_right(x, y)
    if is_symbol(right_x, right_y, check_val):
        lake[right_x][right_y] = island_num
        check_surroundings(right_x, right_y, island_num, check_val)

    #Bottom
    bottom_x, bottom_y = check_bottom(x, y)
    if is_symbol(bottom_x, bottom_y, check_val):
        lake[bottom_x][bottom_y] = island_num
        check_surroundings(bottom_x, bottom_y, island_num, check_val)

    # Left
    left_x, left_y = check_left(x, y)
    if is_symbol(left_x, left_y, check_val):
        lake[left_x][left_y] = island_num
        check_surroundings(left_x, left_y, island_num, check_val)

def switch_to_island():
    value = 0
    island_num = 1
    for i, row in enumerate(lake):
        for j, val in enumerate(lake[i]):
            if val == "o":
                lake[i][j] = " "
            elif val == 'x':
                lake[i][j] = str(island_num)
                check_surroundings(j, i, str(island_num), 'x')
                island_num += 1
                print_lake()
                return
    print_lake()

switch_to_island()


