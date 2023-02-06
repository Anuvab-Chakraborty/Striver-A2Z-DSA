Question_link = "https://practice.geeksforgeeks.org/problems/triangle-number/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_3"

# PATTERN:
"""
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

"""
# Solution:

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")
