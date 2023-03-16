QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1"

"""
For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. Return "Yes" if it is a armstrong number else return "No".
NOTE: 371 is an Armstrong number since 33 + 73 + 13 = 371

Example 1:

Input: N = 153
Output: "Yes"
Explanation: 153 is an Armstrong number
since 13 + 53 + 33 = 153.
Hence answer is "Yes".
Example 2:

Input: N = 370
Output: "Yes"
Explanation: 370 is an Armstrong number
since 33 + 73 + 03 = 370.
Hence answer is "Yes".

Your Task:  
You dont need to read input or print anything. Complete the function armstrongNumber() which takes n as input parameter and returns "Yes" if it is a armstrong number else returns "No"..

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
100 ≤ n <1000
"""


class Solution:
    def armstrongNumber(ob, n):
        p = n;
        s = 0
        while p > 0:
            q = p % 10
            s += q * q * q
            p //= 10
        if s == n:
            return "Yes"
        else:
            return "No"
