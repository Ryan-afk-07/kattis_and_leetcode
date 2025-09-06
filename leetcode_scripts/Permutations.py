class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        exists = []
        def backtrack(ind, numm, combi):
            if numm == []:
                return

            
            while ind < len(numm):
                nummy = numm
                print(combi, nummy, ind, 'before')
                backtrack(ind + 1, nummy, combi)
                combi = combi + [nummy[ind]]
                nummy = numm[:ind] + numm[ind+1:]
                print(combi, nummy, ind, "after")
                backtrack(0, nummy, combi)
                if len(combi) == len(nums) and combi not in exists:
                    final.append(combi)
                    exists.append(combi)
                    break
                else:
                    break
        
        final = []
        backtrack(0, nums, [])

        return final
            

                        