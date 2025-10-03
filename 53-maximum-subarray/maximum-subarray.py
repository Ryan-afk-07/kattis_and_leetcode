class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Solution: iterate through the whole list still.
        for every increment, if the total results in a negative, you will rather take in the positive or larger value out of the negatives. Hence there will be two stored values. One that will be the eventual result and one temporary reset stored value that will reset to zero if it is lesser than 0 
        """
        total = 0
        res = nums[0]
        for n in nums:
            #this is if the added total is less than 0, reset it before a new one is added
            if total < 0:
                total = 0
            total += n
            #this is making sure that IF your current result is more than the total value, it will take that value instead
            res = max(res, total)
        
        return res

        