'''

Practice Problem #2
Samuel Hulme

Problem:
    Given a 2D array of numbers, determine the cheapest path from the top left (0,0) node to the bottom right

    example = [
        [6,   8,  1]
        [100, 2, 30]
        [1,   4,  2]
    ]

    The cheapest path in this case would be the path of 6, 8, 2, 4, 2 = 22

    Conditions:
        1.) The movements can only be right or down
        2.) The numbers can be negative or positive
        3.) Return only the cheapest path value, not the actual path

    My Solution:
        We should use a DFS to determine the shortest path. We can call the top [0, 0] and the bottom [w, h]
        As we go through the list, we will create a dictionary/set of tuples that will represent the cost from that
        location on the matrix. It will be calculated to the value at that location plus the cheapest path that comes
        after it.
'''


def cheapest_path(matrix, hash={}, x=0, y=0):
    if x >= len(matrix[0]) or y >= len(matrix):
        return float('inf')     #If x or y are out of bounds
    elif x == len(matrix[0])-1 and y == len(matrix)-1:
        return matrix[x][y]    #If we found the base
    elif (x,y) in hash:
        return hash[(x, y)]   #If this spot has already been visited

    overall_cheapest = float('inf')
    for dir in [(1, 0), (0, 1)]:
        current_cheapest = cheapest_path(matrix, hash, x+dir[0], y+dir[1])
        if current_cheapest < overall_cheapest:
            overall_cheapest = current_cheapest
    hash[(x, y)] = matrix[x][y] + overall_cheapest
    return hash[(x, y)]

def print_matrix(matrix):
    for row in matrix:
        row_string = "["
        for item in row:
            row_string += "  " + "{:<3}".format(str(item))
        print(row_string + "]")

matrix = [
    [1,    5,    70,  10],
    [90,   4,    -3,  70],
    [-14, 200,     6,  11],
    [-1,  15,     2,   3]
]
print("\nThis program will take in a 2D array of integers and determine the\ncheapest path from the top left to the bottom right index.\n")
print("The test matrix is shown below:\n")
print_matrix(matrix)
print("\nThe cheapest path is: " + str(cheapest_path(matrix)))

