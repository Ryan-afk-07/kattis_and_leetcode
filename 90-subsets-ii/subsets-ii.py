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
                print(units, 'bef')
                backtrack(num+1)
                units.pop()
                #pop function is done to remove the last value out of each segment of the units list as the loop moves. Technically a magic formula to ensure that all sorts of permutations are considered. Kind of like backtrack that i did, but this suits the for loop algorithm, instead of recursive
                print(units, 'aft')
        
        for i in range(1,end+1):
            #intermediate storage list for each iteration of length of list
            units = []
            backtrack(0)
            #print(main)

        return [[]] + main
        
            

        return main
