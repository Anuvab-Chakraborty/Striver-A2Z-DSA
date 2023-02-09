QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285334/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_16"

# PATTERN:-

"""

A
BB
CCC
DDDD
EEEEE

"""

# SOLUTION:-

n = 5

for i in range(n):
    s = chr(i + 65)
    print(s * (i + 1), end="")
    print("")
