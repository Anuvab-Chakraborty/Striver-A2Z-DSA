QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-number-1661489840/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_6"
# PATTERN:
"""

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""

# SOLUTION:

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")
