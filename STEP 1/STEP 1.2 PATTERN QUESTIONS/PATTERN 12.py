QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/double-triangle-pattern-1662664259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_12"

# PATTERN:-

"""

1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1

"""

# SOLUTION:-

n = 5
l = []
for i in range(1, n + 1):
    l += [i]
    print(*l, end="")
    print(" " * (((n - i) * 4) + 1), end="")
    print(*l[::-1])
