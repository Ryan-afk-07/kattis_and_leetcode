class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        idea:
        multiple hashmapping sort of function?
        1. if the word has no similar anagram, save that word as one?
        2. Then do a for loop i guess?
        """
        res = defaultdict(list)

        #if its sorted version is a key, then append it. AH LAME
        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)

        
        return list(res.values())


        