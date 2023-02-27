QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/bubble-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bubble-sort"

"""
Given an Integer N and a list arr. Sort the array using bubble sort algorithm.
Example 1:

Input: 
N = 5
arr[] = {4, 1, 3, 9, 7}
Output: 
1 3 4 7 9
Example 2:

Input:
N = 10 
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 
1 2 3 4 5 6 7 8 9 10

Your Task: 
You don't have to read input or print anything. Your task is to complete the function bubblesort() 
which takes the array and it's size as input and sorts the array using bubble sort algorithm.

Expected Time Complexity: O(N^2).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 103
1 <= arr[i] <= 10**3

"""

# Solution:

arr = [9, 1, 4, 7, 2, 3, 8, 5]
n = len(arr)
# in the next step we are determining how many times we are required to totally sort the array
# in the worst case the least or greatest element maybe present at the end of the order which
# we require that's why we are going to run a loop till the end of the array so that no elements
# remains.
for i in range(n - 1):
    # in this next step we will perform the sorting operation in this case
    # we can assume that we are going to get the largest element at the end
    # of the array and by doing this we won't be needing to check the last
    # element at the end of the array and this way we can avoid checking the (n-i)th
    # element
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]: arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

# TIME COMPLEXITY : O(N**2)

# SPACE COMPLEXITY : O(1)
