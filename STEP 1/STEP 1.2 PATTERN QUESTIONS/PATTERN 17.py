QUESTION_LINK = "https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285911/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_17"

# PATTERN:-

"""

   A
  ABA
 ABCBA
ABCDCBA

"""
l = []
for i in range(65, 91):
    l.append(chr(i))
print(l)

# SOLUTION:-

n = 4
s = ""
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    s = l[:i]
    s = "".join(s)
    if i == 1:
        print(s)
    else:
        print(s, end="")
        s1 = s[:-1]
        s1 = s1[::-1]
        print(s1)
