question = " https://practice.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest"

HINT = """
In case to find the second largest element we have to traverse through the array
and maintain a maximum and second maximum if the current number is greater than
current maximum put the maximum in the second maximum and update the maximum now
if the current number is less than maximum in that case we will check if it's greater
the second maximum and also remember to check if it's not the maximum itself then update
the number in the second maximum then in case of return remember to return second 
maximum only if it's not equal to the maximum. Otherwise return -1
"""
Solution = """
class Solution:

	def print2largest(self,arr, n):
	    maxi=-1;second_m=-1
	    for i in arr:
	        if i>maxi:
	            second_m=maxi
	            maxi=i
	        if i!=maxi and i>second_m:
	            second_m=i
	    return second_m if second_m!=maxi else -1
"""
