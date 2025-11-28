class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Seems like a simple dynamic programming - but a bottom top approach to add up the prev value from its direct below value and its direct below right diagnoal value. And take the minimum value out of the 2.
        """
        if not triangle:
            return 0
        
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])-1,-1,-1):
                print(triangle[i][j], (i,j))
                below = triangle[i][j] + triangle[i+1][j]
                belowright = triangle[i][j] + triangle[i+1][j+1]
                triangle[i][j] = min(below, belowright)
        
        return triangle[0][0]

            
        
        


        