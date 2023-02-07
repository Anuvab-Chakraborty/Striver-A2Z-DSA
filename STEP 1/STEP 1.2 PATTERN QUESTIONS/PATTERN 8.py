QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern-1661493231/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_8"

# PATTERN:-


"""
*********
 *******
  *****
   ***
    *

"""

# SOLUTION:-

n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print("", end=" ")
    print("*" * (2 * i - 1))
