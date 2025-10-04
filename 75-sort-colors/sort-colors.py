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
                #this is needed because if root node or first index is not the largest index, the swap will keep happening until this is fulfilled
                heapify(arr, n, largest)
            
        n = len(nums)

        #build a max-heap (start with last non-leaf node and work upwards)
        for i in range(n//2 - 1, -1, -1):
            print(nums, '1', i)
            heapify(nums,n,i)
            print(nums, '2')
        
        #this is the actual sort from the max heap, because a MAX HEAP is NOT a sorted array
        for i in range(n-1,0,-1):
            print(nums, '3')
            #doing these two steps is actually doing the REVERSE of max heap
            nums[i], nums[0] = nums[0], nums[i]
            print(nums, '4')
            heapify(nums, i, 0)
            print(nums, '5')