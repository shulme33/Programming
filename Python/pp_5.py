'''

Sam Hulme
Practice Problem 5

Dynamic Programming

Minimum Steps to Minimize n to 1
    Given an integer n, return the minimum number of steps to reduce n to 1

Available steps are:
    1.) Decrement n by 1
    2.) If n is divisible by 2, divide by 2
    3.) If n is divisible by 3, divide by 3

Examples:
    10 => 3 steps (10 -> 9 -> 3 -> 1)
    15 => 4 steps (15 -> 5 -> 4 -> 2 -> 1)

Questions:

    Memoization or Tabulation?: Memoization (top-down)

    Run Time: O(n)

    Space Complexity: O(3n) => O(n)

'''


def shortest_path(num, map={}):
    if num == 1:
        return 0
    elif num in map:
        return min(map[num]) + 1

    map[num] = [float('inf'), float('inf'), float('inf')]  # Divide by 3, Divide by 2, Subtract 1

    div_3, div_2 = map[num][0], map[num][1]
    if num % 3 == 0:
        div_3 = shortest_path(num/3, map)
    if num % 2 == 0:
        div_2 = shortest_path(num/2, map)
    sub_1 = shortest_path(num-1, map)

    map[num] = [div_3, div_2, sub_1]
    return min(map[num]) + 1


print("This program will take a number and determine the smallest number of ")
print("calculations needed to reduce it to 1. The possible calculations are:")
print("\n     1.) Decrement by 1")
print("\n     2.) If divisible by 2, divide by 2")
print("\n     3.) If divisible by 3, divide by 3")
starting_num = float(input("\nEnter a number: "))

print("\nThis number can be reduced to 1 in " + str(shortest_path(starting_num)) + " steps:")