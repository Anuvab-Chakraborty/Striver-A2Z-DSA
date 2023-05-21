class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        a=sorted(list(set(nums))) #set -> O(n) ,set -> list ->O(m) ,sorting -> O(mlogm)
        #TOTAL_TC -> O(n +mlogm)
        for i in range(len(a)): #O(m)
            nums[i]=a[i]
        return len(a) #FINAL TC -> O(n + m + mlogm)
        """
        # a=[]
        # for i in nums:
        #     if i not in a:a.append(i)
        # for i in range(len(a)):
        #     nums[i]=a[i]
        # return len(a)
        # total tc: O(n+m)

        # SC: O(m)

        j = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[j]:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                j += 1
        return j + 1  # TC: O(n-1) sc:O(1)
