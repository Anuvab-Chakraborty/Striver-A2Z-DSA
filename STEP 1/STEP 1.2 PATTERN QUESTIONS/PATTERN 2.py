Question_link = "https://practice.geeksforgeeks.org/problems/right-triangle/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_2"

# Pattern:

"""
* 
* * 
* * * 
* * * * 
* * * * *

"""

# Solution1:
"""
for i in range(1,6):
    print("* "*i)
"""
# Solution 2:
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("")
