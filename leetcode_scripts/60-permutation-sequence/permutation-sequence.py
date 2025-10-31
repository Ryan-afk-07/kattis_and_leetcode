class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Rules of lexicographical permutations:
        1. Find the index i in which a[i] < a[i+1]
        2. Find snother index j in which a[j] > a[i] and j > i
        Do a swap of these numbers, to form a new permutation.
        """
        lis_n = [i for i in range(1,n+1)]
        def resetfirst(perm):
            perm_sorted = sorted(perm[1:])
            return [perm[0]] + perm_sorted


        def getnextperm(perm):
            largest_i = 0
            largest_j = 0
            for i in range(0,len(perm)-1):
                if perm[i+1] > perm[i]:
                    largest_i = i
            for j in range(largest_i, len(perm)):
                if perm[j] > perm[largest_i]:
                    largest_j = j
            perm[largest_i], perm[largest_j] = perm[largest_j], perm[largest_i]
            #print(largest_i+1, len(perm), perm)
            if len(perm) - 1 - (largest_i + 1) > 0:
                for num in range((len(perm)-largest_i)//2):
                    perm[largest_i+1+num], perm[len(perm)-1-num] = perm[len(perm)-1-num], perm[largest_i+1+num]
            #print(perm)
            return perm

        curr_first = 1
        for i in range(k-1):
            getnextperm(lis_n)
        
        str_lis_n = map(str, lis_n)

        return "".join(str_lis_n)

        