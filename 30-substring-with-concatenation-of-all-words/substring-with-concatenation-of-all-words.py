class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Idea: Do a combination of all variations of the list. And then have them all combined.
        OH then sliding window since the result of all combinations will ALL have the same length. They must all BE CONCATENATED.
        
        #I LOVEEEEEE BACKTRACK SHIT
        exists = []
        def backtrack(ind, wordss, combi):
            if wordss == []:
                return
            
            while ind < len(wordss):
                wordsy = wordss
                backtrack(ind + 1, wordsy, combi)
                combi = combi + [wordsy[ind]]
                wordsy = wordss[:ind] + wordss[ind+1:]
                backtrack(0, wordsy, combi)
                if len(combi) == len(words) and combi not in exists:
                    exists.append(combi)
                    final.append(combi)
                    break
                else:
                    break

        
        final = []
        backtrack(0, words, [])
        for i in range(len(final)):
            final[i] = "".join(final[i])

        print(final)

        window = len(final[0])
        pointer = 0
        ind = []
        while pointer < len(s) - window + 1:
            string = s[pointer:pointer+window]
            print(string)
            if string in final:
                ind.append(pointer)
                pointer += 1
            else:
                pointer += 1
        return ind
    """
        """
        Updated: my solution MAY work, but only if GPU is solid. Need a more efficient solution
        FROM solutions page - retrieving understanding.
        1. Finding permutations: since ALL STRINGS are of the same length in the words list. There is NO need to do permutations from the words list. Do the REVERSE INSTEAD.
        2. Do a sliding windoe for each section of the string. The criteria for a permutation will be valid IF:
        2.1 current window has all the words from the words array
        2.2 Count of each of the words in the window is the same as the count in the array [HENCE the hashmap!]
        3. Do 2 hashmaps. 1 will contains the count of each word in the words list.
        Another one will keep the count of words in the current window.
        """
        #keep track of number of words in given words list
        words_hash = {}
        #keep track of number of words and type of words in the current window of string
        wordSize = len(words[0])
        window = wordSize * len(words)
        word_count = len(words)
        for i in words:
            words_hash[i] = words_hash.get(i,0) + 1
        ans = []
        print(words_hash)
        #because each word in the words list is of the same length. Variation of error chars in the string must be considered. I.e. if there is a word xfoobarfoo: valid word starts in the 1st and 4th (increments of 3) for xxfoobarfoo its 2nd and 5th - notice the pattern
        for offset in range(wordSize):
            start = offset
            currentCount = {}
            count = 0
            #this is just an auto skip of wordsize, since each word is wordsize chars long
            for end in range(offset, len(s) - wordSize + 1, wordSize):
                print(start, count, 'window')
                curr_word = s[end:end + wordSize]
                if curr_word in words_hash:
                    currentCount[curr_word] = currentCount.get(curr_word, 0) + 1
                    count += 1
                    #after this line, if the while loop does not fulfill a right condition, the loop goes back to the front.
                    #this while loop exists if the substring is TOO long. Hence the move of start word and start position to the right by length of word. And deleting the count number by one. It will be skipped if above IS NOT TRUE.
                    while currentCount[curr_word] > words_hash[curr_word]:
                        start_word = s[start:start + wordSize]
                        currentCount[start_word] -= 1
                        start += wordSize
                        count -= 1
                        print(start, count, 'current_window')

                    #this is obvious. If count is the same, then take the index la.
                    if count == word_count:
                        ans.append(start)
                #situation where either 1. word is NOT IN original words list or 2. doesn't fulfill the word hashmap number of words
                else:
                    count = 0
                    start = end + wordSize
                    currentCount.clear()
                    print(start, 'new window')
        return ans
                

            

