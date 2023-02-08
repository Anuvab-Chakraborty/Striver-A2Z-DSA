QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718455/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_11"

# PATTERN:-

"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

"""

# SOLUTION:-

n = 5

for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(1, i + 1):
            if j % 2 == 0:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print()
    else:
        for j in range(1, i + 1):
            if j % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print("")
