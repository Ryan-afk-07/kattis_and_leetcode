class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dicti = dict()
        for index, val in enumerate(candidates):
            dicti[index] = val
        def backtrack(ind, summ, combi):
            if ind == len(candidates):
                return
            
            while summ <= target:
                backtrack(ind+1, summ, combi)
                combi = combi + [dicti[ind]]
                summ = summ + dicti[ind]
                print(combi)
                if summ == target:
                    if combi not in final:
                        final.append(combi)
                        backtrack(ind+1, summ - dicti[ind], combi[:-1])
                    else:
                        break
            
        
        final = []
        backtrack(0, 0, [])

        return final

            

            