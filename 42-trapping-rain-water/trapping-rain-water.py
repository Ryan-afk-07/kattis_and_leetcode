class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Idea from solutions:
        1. Set 2 pointers at each end.
        2. If the left maximum height is higher than the right, we move the right pointer and check if its current height is the max height, then find difference between it and the max height
        3. The opposite goes through - i.e. if right maximum height is higher than the left
        4. For equal height, well moving either one works.
        """
        left = 0
        right = len(height) -1
        left_max = height[left]
        right_max = height[right]
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
