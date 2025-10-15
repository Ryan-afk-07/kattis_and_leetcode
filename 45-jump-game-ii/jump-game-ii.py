class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        """
        Based on video.
        Reasoning:
        1. Do a 2 step forcast approach. If a current pointer and its followed up steps will be able to reach the end. Stop there.
        2. If not, continue on with that approach - using a further for loop of the furthest travelled distance.
        """
        steps = 0
        pointer = 0
        current = 1
        #this while loop is in case this 'step' you are already on (called pointer) has a range of values that allow you to reach the end immediately. 1 step is only required
        while pointer < len(nums)-1:
            if pointer + nums[pointer] >= len(nums) -1:
                steps += 1
                return steps
            #this step is when the top does not happen, and more steps are needed. We will do kind of a relative forcast jump. to check out which value next could be stepped on that would allow us to then jump all the way to the end (1) or jump much further with lesser steps (2)
            for i in range(current,current+nums[pointer]):
                #in case top can't sense ah. safe case
                if i == len(nums) - 1:
                    break
                #scenario (1). the current step can't go to the end, but stepping onto the next step will allow us to go to the end. This will account for 2 steps
                if i + nums[i] >= len(nums) - 1:
                    steps += 2
                    return steps
                #scenario (2). current step can't go to the end, neither can all the other steps that are within the move range of this and the next. So we find the furthest distance we possibly can that will place us very close to the end.
                elif i + nums[i] >= current + nums[current] and i + nums[i] < len(nums):
                    current = i
                else:
                    continue
            steps +=1
            pointer = current
            current += 1
        return steps



        