class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        THIS IS BACKTRACK. BUT IN THE FORM OF NCHOOSESOMETHING ALSO
        This is an extension to the 'Combinations question', but now making sure that each
        index is taken into reference, instead of numbers, since now we follow the unique numbers
        in the list, NOT the range of numbers that we take from the combinations (n)
        """
        final = []
        end = len(nums)
        def backtrack(start):
            if len(units) == i:
                if sorted(units) not in final:
                    final.append(units[:])
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
            #print(final)

        return [[]] + final
            

        