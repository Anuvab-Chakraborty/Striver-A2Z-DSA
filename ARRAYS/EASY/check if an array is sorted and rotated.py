HINT = """
Find the breaking point .
If the array is sorted and then rotated then 
there shouldn't be more than one breaking point
so using that as our reference we can solve this 
question in O(n) TC. We must search in an array there 
mustn't be more than one number greater less than 
it's previous number. the one will be the point where 
the array was rotated also notice there can be 0 break points 
as the array can also be initially sorted.
"""


# Solution:

class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                c += 1
        return True if c <= 1 else False
