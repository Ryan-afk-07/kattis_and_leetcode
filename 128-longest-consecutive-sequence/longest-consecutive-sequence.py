class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Set a for loop to check each and every integer inside.
        Set a longest length and a current length variable.
        Current length will increment by 1 for each +1 of each iterable that is seen in the list.
        It will stop if a +n is not able to be found in the list.
        If the current length is more than the longest length, set it as the new length
        
        if not nums:
            return 0
        longest_len = 0
        curr_len = 0
        curr_ind = 0
        curr_val = nums[curr_ind]
        while curr_ind < len(nums):
            #print(curr_ind, 'index', curr_val, 'value')
            if curr_val in nums:
                curr_val += 1
                curr_len += 1
            else:
                if curr_len > longest_len:
                    longest_len = curr_len

                curr_len = 0
                curr_ind += 1

                if curr_ind >= len(nums):
                    break

                curr_val = nums[curr_ind]
        
        return longest_len

        """
        """
        better and featured solution
        """
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best


            

        