class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Idea: since is non-descending, i.e. ascending. It is sorted already.
        So keep cutting the list into half. based on what the middle value is.
        But on the occassion that the middle value is the target value, we must see if it has neighbouring members (left and right that have the same value)
        Of course in the event that the list is cut into nothing, or just one value. Then return nothing.
        """
        if not nums:
            return [-1,-1]
        start = -1
        end = 1
        current = len(nums)//2
        numm = nums
        while len(numm) > 1:
            temp = len(numm)//2
            #print(start, end, temp, current, numm)
            #scenario1: if we are lucky and that value is right smack there.
            if target == numm[temp]:
                while (temp + start) >= 0 and numm[temp + start] == target:
                    start -= 1
                while (temp + end) < len(numm) and numm[temp + end] == target:
                    end += 1
                #print(start, end)
                return [current + start + 1, current + end - 1]
            
            #scenario2 and 3: when the middle value is either more or less than the target.
            ##if its more than target, remove the right side. If its less than target, remove the left side
            #for both odd and even length lists, the index that will be split will always be at the right side.
            if numm[temp] < target:
                numm = numm[temp:]
                current = current + len(numm)//2
                continue
            
            if numm[temp] > target:
                numm = numm[:temp]
                if len(numm) % 2 == 0: 
                    current = current - len(numm)//2
                else:
                    current = current - len(numm)//2 - 1
                continue
        
            
        
        if numm[0] == target:
            #print(nums, current, start, end)
            while (current + start) >= 0 and nums[current + start] == target:
                start -= 1
            while (current + end) < len(nums) and nums[current + end] == target:
                end += 1
            #print(start, end)
            return [current + start + 1, current + end - 1]
        else:
            return [-1,-1]

