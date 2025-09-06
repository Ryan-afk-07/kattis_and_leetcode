class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        good idea:
        have a left pointer that only moves by one once a word has repeat
        have a right pointer that constantly moves to check if the string has repeat
        have a set to store all distinct strings/letters
        """
        #the length of the longest substring will be right - left + 1
        #reason is because as long as the list between right and left has its letters all in the set, it will be valid
        left = 0
        right = 0
        longest = 0
        set_string = set()
        while left < len(s) and right < len(s):
            #case for last right value being distinct up till last value
            if right == len(s) - 1 and (s[right] not in set_string):
                length = right - left + 1
                if length > longest:
                    longest = length
                right += 1
            #case: right pointer's value is not in the set
            elif s[right] not in set_string:
                set_string.add(s[right])
                right += 1
            #case: right pointer's value is IN the set
            elif s[right] in set_string:
                length = right - left
                if length > longest:
                    longest = length
                set_string.remove(s[left])
                left += 1
                right = right


        
        return longest

                


        