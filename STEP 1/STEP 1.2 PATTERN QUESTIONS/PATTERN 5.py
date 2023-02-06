QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_5"

# PATTERN:

"""
* * * * *
* * * * 
* * * 
* *  
* 

"""

# SOLUTION:

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("")
