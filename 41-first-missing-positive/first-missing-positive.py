class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Did a bit of cheating and went to refer to the solutions a lil (because of the O(1) space complexity thing confusing me abit)
        Thoughts:
        1. It is alright to sort the list and remove all negative integers wtf
        2. Check if the list is empty. If it is means all elements in the list is negative. Return 1
        3. If the list is not. Initiate a pointer that starts with the first value. If the pointer is strictly greater, return the target, if not, add pointer with 1 and add target with 1 and continue on 
        """
        #remove negative numbers
        removed = set([i for i in nums if i > 0])

        #case where all zeros or negative numbers
        if not removed:
            return 1

        final_sort = sorted(list(removed))
        print(final_sort)
        target = 1
        pointer = 0
        while pointer < len(final_sort):
            if final_sort[pointer] > target:
                return target
            pointer += 1
            target += 1
            
        return final_sort[pointer-1]+1
        