QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_10"

# PATTERN:-

"""

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

n = 5

for i in range(1, n + 1): print("* " * (i))
for i in range(n - 1, 0, -1): print("* " * i)
