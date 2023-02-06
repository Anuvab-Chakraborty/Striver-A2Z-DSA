question_link = "https://practice.geeksforgeeks.org/problems/square-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_1"
# pattern:
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# ans:
# solution1:
"""
for _ in range(5):
    for _ in range(5):
        print("*",end=" ")
    print("")
"""
# Solution 2:
for _ in range(5):
    print("* " * 5)
