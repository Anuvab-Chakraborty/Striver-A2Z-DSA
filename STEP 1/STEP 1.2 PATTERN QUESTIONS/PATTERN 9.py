QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_9"

# PATTERN:-

"""
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *

"""

# SOLUTION:-

n = 5

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    print("* " * (i + 1), end="")
    print("")
for i in range(2 * n, n, -1):
    for j in range(2 * n - i):
        print(" ", end="")
    print("* " * (i - n), end="")
    print("")
