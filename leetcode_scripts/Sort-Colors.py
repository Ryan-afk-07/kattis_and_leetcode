class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Oh means likely bubble sort already
        """
        #this heapsort just means the creation of a tree with one parent
        #node connected to 2 children node (left and right)
        def heapify(arr,n,i):
            largest = i
            left = 2*i + 1
            right = 2*i + 2
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
            
        n = len(nums)

        for i in range(n//2 - 1, -1, -1):
            heapify(nums,n,i)
            
        for i in range(n-1,0,-1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)