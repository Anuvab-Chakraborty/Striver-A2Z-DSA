QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-1-to-n-without-using-loops"

"""
Print numbers from 1 to N without the help of loops.

Example 1:

Input:
N = 10
Output: 1 2 3 4 5 6 7 8 9 10

Example 2:

Input:
N = 5
Output: 1 2 3 4 5
 

Your Task:
This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints number from 1 to N recursively. Don't print newline, it will be added by the driver code.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).


Constraints:
1 <= N <= 1000
"""

"""
def printNos(n):
    if n > 1:
        printNos(n - 1)
    print(n, end=" ")
    return


printNos(10)
"""


class Solution:
    # Complete this function
    def printNos(self, n):
        c = n - 1
        # c=1
        # self.helper(n,c)
        self.helper(c, n)

    """
    def helper(self,n,c):
        if c==n:
            print(c,end=" ")
            return
        print(c,end=" ")
        return self.helper(n,c+1)

    """

    def helper(self, c, n):
        if c == 0:
            print(n, end=" ")
            return
        print(n - c, end=" ")
        self.helper(c - 1, n)
    # """
