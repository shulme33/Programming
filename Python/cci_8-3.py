'''

Cracking the Coding Interview
Problem 8.3
Sam Hulme

Prompt:
    A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i.
    Given a sorted array of distinct integers, write a method to find a magic index,
    if one exists, in array A.

    FOLLOW UP:
        What is the values are not distinct.


Examples:

    Distinct Values

    1.)
        [1, 3, 4, 5, 7, 8, 9, 10] => No magic indexes


    2.)
        [0, 1, 2, 3, 4, 5]
        [0, 2, 4, 5, 6, 7] => Index 0 is a magic magic index. Index = 0, value = 0.
         ^

    3.)
        [-2, -1, 1, 2, 4, 7, 10]  =>  Index 4 is a magic index
                    ^


    Non-distinct Values:

    3.)
        [1, 3, 3, 3, 4, 5, 8, 10]  =>  Index 3 is a magic index. Index = 3, value = 3

    4.)
        [0 ,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        [-2,  1, 1, 2, 2, 2, 2, 5, 5, 6, 10]
              ^                          ^
                       ^

    Notes:
        Obvious answer is to iterate through the entire array.
            - Runtime = O(n) where n is length of array.

        Better: Since its sorted, we could go for a binary search. Each place, we would check if the index is
        greater than the value or not. If index > value, then the magic index is above our current location.
        If index < value, the magic index is below. We can keep a record of whether or not we have already
        checked a spot which will allow us to not check a spot twice.
            - Runtime = O(logn) where n is length of array.

        Slight improvement. If we check the first and last spot in the array, and the values inside the
        array cannot contain a magic index, we can exit immediately.

            [-100, -99, -95]

            The possible magic indexes exist between 0 and 2. Since the list is sorted, we know all possible
            values inside the array by checking the first and last index. If the first index is greater than 2
            or the last index is less than 0, then we KNOW that there are no magic indexes.
                 - This check is O(1) so constant.

        Non-Distinct Sets:

            In this case, we can do a similar thing but will need to check both sides. We can still do binary search,
            but in this scenario, we cannot make any statements about where the magic indexes are based on the value
            at the mid point. Therefore, we will do a binary-type search that looks both directions. However, we can
            somewhat improve tha algorithm by taking into account the value at the midpoint. Lets say we have the
            following scenario.

            List = [-14, -5, -3, 0, 1, 3, 3, 4, 4, 4, 4, 7, 12, 15, 16]
                                                           ^

            Magic Index @ 12
            Low = 0
            High = 14
            Mid = 7

            The value at mid (7) is 4. Therefore, we know that the magic index cannot exist between index 7 (mid) and
            and index 4 (value @ mid). That allows us to narrow our recursion to the following.

            Sub_List_1 = Index 0 => 4 or [-14, -5, -3, 0, 1]
            Sub_list_2 = Index 7 - 14 or [4, 4, 4, 4, 7, 12, 15, 16]

            We can ignore all values in indexes 5-6



'''


import math
import random


def find_magic_index_distinct(numbers, low, high):     # Determine the magic indexes in a sorted list of distinct values

    mid = math.floor((low + high)/2)
    if numbers[low] >= high or numbers[high] <= low or mid >= high or mid <= low:
        return -1
    if numbers[low] == low: return low
    if numbers[high] == high: return high
    if numbers[mid] == mid: return mid

    if numbers[mid] > mid:  #If true, we know the magic index can only exist below the mid index
        return find_magic_index_distinct(numbers, low, mid)
    else:
        return find_magic_index_distinct(numbers, mid, high)


def find_magic_index_nondistinct(numbers, low, high):
    mid = math.floor((low + high) / 2)

    if numbers[low] >= high or numbers[high] <= low or mid >= high or mid <= low:
        return -1
    if numbers[high] == high: return high
    if numbers[low] == low: return low
    if numbers[mid] == mid: return mid

    bottom_cap, top_cap = mid, mid
    if 0 <= numbers[mid] < len(numbers):
        bottom_cap = min(mid, numbers[mid])
        top_cap = max(mid, numbers[mid])

    bottom = find_magic_index_nondistinct(numbers, low, bottom_cap)
    if bottom >= 0:
        return bottom
    top = find_magic_index_nondistinct(numbers, top_cap, high)
    return top




def create_example_problem(list_length, distinct):
    # Simple method to build a list with at least one magic index
    new_numbers = [0] * list_length
    bottom_range = 0
    if distinct:
        bottom_range = 1

    magic_index = random.randint(0, list_length-1)
    new_numbers[magic_index] = magic_index
    counter = magic_index-1
    counter_val = new_numbers[magic_index]
    while counter >= 0:
        counter_val = counter_val - random.randint(bottom_range, 3)
        new_numbers[counter] = counter_val
        counter -= 1
    counter = magic_index + 1
    counter_val = new_numbers[magic_index]
    while counter < list_length:
        counter_val = counter_val + random.randint(bottom_range, 3)
        new_numbers[counter] = counter_val
        counter += 1

    return new_numbers, magic_index



print("\nThis program takes in an ordered list of integers and returns the first magic index that it finds.\n"
      "A magic index is defined as an index where the value at that index is equal to the index. This program\n"
      "will generate a list that only contains unique values an one that contains repeated values. \n\n"
      "For a list of distinct values:")
numbers_original_1, magic_1 = create_example_problem(30, True)
print(str(numbers_original_1))
print("A magic index exists at: " + str(find_magic_index_distinct(numbers_original_1, 0, len(numbers_original_1) - 1)))

print("\nFor a list of non-distinct values:")
numbers_original_2, magic_2 = create_example_problem(30, False)
print(str(numbers_original_2) + "\n")
print("A magic index exists at: " + str(find_magic_index_nondistinct(numbers_original_2, 0, len(numbers_original_2) - 1)))