class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Did a bit of cheating and went to refer to the solutions a lil (because of the O(1) space complexity thing confusing me abit)
        Thoughts:
        1. It is alright to sort the list and remove all negative integers wtf
        2. Check if the list is empty. If it is means all elements in the list is negative. Return 1
        3. If the list is not. Initiate a pointer that starts with the first value. If the pointer is strictly greater, return the target, if not, add pointer with 1 and add target with 1 and continue on 
        Things to keep note: Need to amend nums directly to preserve space complexity. And DO A FOR LOOP, NOT WHILE since there may be duplicate integers. If the integer is there, even if its a duplicate, iterating to the next same value will make your integer the same until it reaches the next sorted value
        """
        #remove negative numbers
        nums = [i for i in nums if i > 0]

        #case where all zeros or negative numbers
        if not nums:
            return 1

        nums.sort()
        target = 1
        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target
            
        return target
        