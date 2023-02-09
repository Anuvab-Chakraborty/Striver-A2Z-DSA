QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern-1662284916/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_14"

# PATTERN:-

"""

A
AB
ABC
ABCD
ABCDE

"""

# SOLUTION:

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(chr(j + 65), end="")
    print()
