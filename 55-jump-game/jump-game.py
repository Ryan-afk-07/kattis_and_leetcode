class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Idea: based off from a video snippet i've watched. Do reverse jumping. Check if there is a number that is able to jump to that particular index. If it is, change the end point to that index, then move again. If we are able to reach the end. Return True. If not return false
        """
        if len(nums) == 1:
            return True
        current = len(nums) - 1
        #print(list(range(len(nums)-1,-1,-1)))
        for i in range(len(nums)-1, -1, -1):
            #print(nums[i], current)
            difference = current - i
            #if current is near to the start and we can reach the end, return True
            if nums[0] >= current:
                return True
            #if steps allowed in the moved index is equals or more than the distance from that index to the current stepped index/last index, move it to be the new current - i.e. backstepping
            elif nums[i] >= difference:
                current = i
            else:
                pass
        return False
            








