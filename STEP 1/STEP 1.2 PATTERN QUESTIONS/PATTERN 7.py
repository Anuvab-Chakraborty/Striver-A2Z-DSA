QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern-1661492263/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_7"

# PATTERN:

"""
    *
   ***  
  *****
 *******
*********
"""

# SOLUTION:
"""
for i in range(5):
    for j in range(5-i-1):
        print(" ",end=" ")
    print("* "*(2*i +1),end=" ")
    for j in range(5-i-1,2*5):
        print(" ",end=" ")
    print("")
"""
for i in range(5):
    for j in range(5 - i - 1):
        print("", end=" ")
    print("*" * (2 * i + 1), end="")
    print("")
