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

def printLake(lake):
    for row in lake:
        print(row)


if __name__ == '__main__':

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

    printLake(lake)


