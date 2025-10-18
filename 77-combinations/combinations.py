class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        My idea:
        can do backtrack. But is there a better way? Pointer?
        Second idea: two sliding windows?
        
        res = []
        list_n = list(range(1,n+1))
        def backtrack(ind, combi):
            if ind == n+1:
                if len(combi) == k and sorted(combi) not in res:
                    res.append(combi)
                    return
                return
            if len(combi) == k and sorted(combi) not in res:
                res.append(combi)
                return
            
            backtrack(ind+1, combi)
            combi = combi + [ind]
            backtrack(ind+1, combi)
        
        backtrack(1, [])
        return res
        
        
        Example: list is [1,2,3,4]
        """
        """
        Better, more efficient way to backtrack it seems. Add and remove the latest added number from the list. Place the recursive function in the middle to allow for the list to continue expanding.
        """
        res = []
        comb = []
        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for num in range(start, n+1):
                comb.append(num)
                #print(comb, 'before')
                backtrack(num+1)
                comb.pop()
                #print(comb, 'after')
            
        backtrack(1)
        return res
        
        