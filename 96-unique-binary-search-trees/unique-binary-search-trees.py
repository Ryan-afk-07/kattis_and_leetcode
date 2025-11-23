class Solution:
    def numTrees(self, n: int) -> int:
        """
        A catalan number formula question
        """
        def catalan(num):
            if num <= 1:
                return 1
            return int(((4*num - 2)/(num + 1)) * catalan(num - 1))
        
        return catalan(n)
        