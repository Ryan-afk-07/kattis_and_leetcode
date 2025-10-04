class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        My thoughts after understanding algorithm:
        1. start with a pointer, from 1 all the way to len(nums)-1
        2. Find the largest index in which its index - 1 is smaller.
        3. Once the largest index is found. Find the index that is bigger and or equal than the index of the first one (its value needs to be bigger.)
        4. Once they are found. Swap both values
        4. Then do a reverse def for ALL after index i
        """
        def reverse1(lis, index):
            print(len(lis)-index+1)
            for i in range((len(lis)-index+1)//2):
                nums[index+i], nums[len(lis)-1-i] = nums[len(lis)-1-i], nums[index+i]
            return lis
        def reverse_norm(lis):
            for i in range(len(lis)//2):
                lis[i], lis[len(lis)-1-i] = lis[len(lis)-1-i], lis[i]
            return lis
        pointer1 = None
        #first case: if pointer1 is none - means list is the LAST lexicographical perm
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                pointer1 = i
            else:
                continue
        if pointer1 == None:
            return reverse_norm(nums)
        pointer2 = len(nums)-1
        while pointer2 >= pointer1:
            if nums[pointer2] > nums[pointer1 -1]:
                break
            else:
                pointer2 -= 1
        #do the actual swapping
        print(pointer1-1, pointer2)
        nums[pointer2], nums[pointer1-1] = nums[pointer1 -1], nums[pointer2]
        print(nums)
        return reverse1(nums, pointer1)




                
        