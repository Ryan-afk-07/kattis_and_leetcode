class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        ans = ""
        current_no = prev[0]
        count = 0
        for i in range(len(prev)):
            if prev[i] != current_no:
                ans += str(count) + str(current_no)
                current_no = prev[i]
                count = 1
            else:
                count +=1
        ans += str(count) + str(current_no)

        return ans

        