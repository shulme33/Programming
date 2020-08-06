'''

LeetCode Problem 1
Sam Hulme

Question:

    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7]
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
    Example 2:

    Input: nums = [1,2,3,4,4,3,2,1], n = 4
    Output: [1,4,2,3,3,2,4,1]
    Example 3:

    Input: nums = [1,1,2,2], n = 2
    Output: [1,2,1,2]

Constraints:

    1 <= n <= 500
    nums.length == 2n
    1 <= nums[i] <= 10^3

Thoughts:

    1.) Go through the last half of the array and insert back those values at the required index. For example, if your
        array was [1, 2, 3, 4, 5, 6, 7, 8], then you would insert 5 @ index 1 and 6 @ index 3 and so on. However, the
        runtime of inserting into an array at an index is O(n). Therefore, we will not want to do that. That would make
        our method O(n^2). Space complexity is O(n) for the original array.

    2.) Create a new array, and then place the elements at the correct indexes as we go. This will give us a O(1) insert
        time on each insertion. The space complexity will go up to O(2n) but the runtime will reduce to O(n).
'''


def shuffle(nums, n):
    new_nums = [0]*2*n
    for i in range(0, len(nums)):
        new_nums[i] = nums[int(i/2) + int(i % 2 != 0)*n]
    return new_nums

print("\nThis code will take in a list of values and print them out in the following way."
      "\nLets say the original list can be represented as [x1, x2, x3.....xn, y1, y2, y3....yn]"
      "\nThis program will produce [x1, y1, x2, y2, x3, y3....xn, yn]")

global_nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print("\nOriginal List: " + str(global_nums))
print("\n" + str(shuffle(global_nums, 5)))
