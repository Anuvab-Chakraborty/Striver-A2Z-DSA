QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285196/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_15"

# PATTERN:-

"""

ABCDE
ABCD
ABC
AB
A

"""

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(j + 65), end="")
    print()
