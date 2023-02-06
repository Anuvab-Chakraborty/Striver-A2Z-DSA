QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-number-1661428795/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_4"

# PATTERN:

"""
1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

"""

# SOLUTION:

for i in range(1, 6):
    for j in range(1, i + 1): print(i, end=" ")
    print("")
