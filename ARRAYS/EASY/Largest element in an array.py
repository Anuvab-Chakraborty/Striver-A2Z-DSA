question_link = "https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array"


def largest(arr, n):
    maximum = float("-inf")
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum
