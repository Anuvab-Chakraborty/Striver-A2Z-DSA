QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/palindrome0746/1"

"""
Given an integer, check whether it is a palindrome or not.

Example 1:

Input: n = 55555
Output: Yes

Example 2:

Input: n = 123
Output: No
 

Your Task:
You don't need to read or print anything. Your task is to complete the function is_palindrome() which takes the number as input parameter and returns "Yes" if it is palindrome otherwise returns "No"(Without quotes).
 

Expected Time Complexity: O(x)
Expected Space Complexity: O(x) where x is number of digits in n.
 

Constraints:
1 <= n <= 1000
"""

class Solution:
    def is_palindrome(self, n):
        p = n
        c = 0
        l = len(str(n))
        i = 1
        while p >= 0:
            q = p % 10
            c += q * (10 ** (l - i))
            i += 1
            p //= 10
        if c == n:
            return "Yes"
        else:
            return "No"
