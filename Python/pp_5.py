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

    Memozation:
        Run Time: O(n)
        Space Complexity: O(3N) => O(N) where N is a recursive call

    Tabulation:
        Run Time: O(n)
        Space Complexity: O(n) where n is the number of nodes

'''


def shortest_path_memoization(num, map={}):
    if num == 1:
        return 0
    elif num in map:
        return min(map[num]) + 1

    map[num] = [float('inf'), float('inf'), float('inf')]  # Divide by 3, Divide by 2, Subtract 1

    div_3, div_2 = map[num][0], map[num][1]
    if num % 3 == 0:
        div_3 = shortest_path_memoization(num/3, map)
    if num % 2 == 0:
        div_2 = shortest_path_memoization(num/2, map)
    sub_1 = shortest_path_memoization(num-1, map)

    map[num] = [div_3, div_2, sub_1]
    return min(map[num]) + 1


def shortest_path_tabulation(num):
    tab = [0] * (num+1)
    tab[1] = 0

    for i in range(2, num+1):
        div_3 = div_2 = sub_1 = float('inf')
        if i % 3 == 0:
            div_3 = tab[int(i/3)] + 1
        if i % 2 == 0:
            div_2 = tab[int(i/2)] + 1
        sub_1 = tab[i-1] + 1
        tab[i] = min(div_3, div_2, sub_1)
    return tab[num]



print("This program will take a number and determine the smallest number of ")
print("calculations needed to reduce it to 1. The possible calculations are:")
print("\n     1.) Decrement by 1")
print("\n     2.) If divisible by 2, divide by 2")
print("\n     3.) If divisible by 3, divide by 3")
starting_num = int(input("\nEnter a number: "))

print("\nUsing memoization, this number can be reduced to 1 in " + str(shortest_path_memoization(starting_num)) + " steps:")
print("\nUsing tabulation, this number can be reduced to 1 in " + str(shortest_path_tabulation(starting_num)) + " steps:")