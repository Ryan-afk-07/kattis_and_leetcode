class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Better solution: sort all intervals based on their smallest ranges.
        If the previous range has a max value lesser than the min of the next one, merge them and remove both
        If not, remove the previous range
        """
        merged = []
        inter_copy = intervals.copy()
        inter_copy.sort(key= lambda x: x[0])

        prev = inter_copy[0]

        for pair in inter_copy[1:]:
            #this line is the case where each pair has its min value less than the max value of the previous pair
            if pair[0] <= prev[1]:
                prev[1] = max(prev[1], pair[1])
            else:
                merged.append(prev)
                prev = pair
        
        #this is for the 'last' non matched pair in the list
        merged.append(prev)

        return merged

        """
        Idea: compare lists 2 by 2.
        1. Have 2 pointers. One always at the first element, and the next to filter over to the last.
        2. If they merge or have overlapping intervals, remove the two lists, and add in the new one for comparison
        3. If not, move pointer 2 forwards. If it reaches the last, remove the element at the first column and place it into the new list
        4. Do this until the whole list is empty.
        """
        """
        def find_new_interval(list1, list2):
            range1 = set(range(list1[0], list1[1] + 1))
            range2 = set(range(list2[0], list2[1] + 1))
            overlap = range1 & range2
            union = range1 | range2
            #print(overlap, union)
            if not overlap:
                return None
            return [min(union), max(union)]
        
        pointer1 = 0
        pointer2 = 1
        inter_copy = intervals.copy()
        result_list = []
        while len(inter_copy) > 1:
            #print(inter_copy,result_list, pointer1, pointer2)
            result = find_new_interval(inter_copy[pointer1], inter_copy[pointer2])
            if result is not None:
                to_remove = [inter_copy[pointer1], inter_copy[pointer2]]
                inter_copy = [sublist for sublist in inter_copy if sublist not in to_remove]
                inter_copy.append(result)
                pointer2 = 1
            else:
                pointer2 += 1
                if pointer2 == len(inter_copy):
                    result_list.append(inter_copy[pointer1])
                    inter_copy.remove(inter_copy[pointer1])
                    pointer2 = 1
                else:
                    continue
            #print(inter_copy,result_list)
        if len(inter_copy) == 1:
            result_list.append(inter_copy[0])
        return result_list
        """



        
