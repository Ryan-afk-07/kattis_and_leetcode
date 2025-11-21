class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        some solutions. Can do the usual backtracking
        not sure if bfs or dfs might work.
        """
        main = []
        end = len(nums)
        def backtrack(start):
            if len(units) == i:
                if sorted(units) not in main:
                    main.append(sorted(units[:]))
                    return
                else:
                    return

            for num in range(start, end):
                units.append(nums[num])
                backtrack(num+1)
                units.pop()
        
        for i in range(1,end+1):
            #intermediate storage list for each iteration of length of list
            units = []
            backtrack(0)
            print(main)

        return [[]] + main
        
            

        return main
