class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        """
        for i in range(len(nums)):
            nums[i] = nums[i] + i"""
        """
        Improved idea based on a watched video: do reverse backtrack of the list instead. Start with the last index
        """
        steps = 0
        pointer = 0
        current = 1
        while pointer < len(nums)-1:
            if pointer + nums[pointer] >= len(nums) -1:
                steps += 1
                return steps
            for i in range(current,current+nums[pointer]):
                if i == len(nums) - 1:
                    break
                if i + nums[i] >= len(nums) - 1:
                    steps += 2
                    return steps
                elif i + nums[i] >= current + nums[current] and i + nums[i] < len(nums):
                    current = i
                else:
                    continue
            steps +=1
            pointer = current
            current += 1
        return steps



