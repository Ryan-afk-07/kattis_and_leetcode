class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Idea that popped out my head.
        I do some reverse engineering. Fit each interval to the new interval to see if their intersection has AT LEAST one value.If it does, save its index to a corresponding list. Then use the list to get the eventual new intervals.
        """
        #first case: if the interval list itself is just empty. Just add in the newInterval.
        def checkintervals(int1, int2):
            #print(int1, int2)
            set1 = set(range(int1[0], int1[-1] + 1))
            set2 = set(range(int2[0], int2[-1] + 1))
            return set1 & set2

        if not intervals:
            return [newInterval]

        overlap_intervals = []
        for i in range(len(intervals)):
            if checkintervals(newInterval, intervals[i]):
                overlap_intervals.append(i)
        
        #print(overlap_intervals)

        #when newInterval does NOT contain nor overlap ANY interval in the intervals list
        inde = None
        if not overlap_intervals:
            #check where to fit the newinterval
            for i in range(0, len(intervals)):
                if newInterval[-1] < intervals[i][0]:
                    inde = i
                    break
            if inde is None:
                inde = len(intervals)
            return intervals[:inde] + [newInterval] + intervals[inde:]

        new_list = intervals[:overlap_intervals[0]] + [[min(intervals[overlap_intervals[0]][0], newInterval[0]), max(intervals[overlap_intervals[-1]][-1], newInterval[-1])]] + intervals[overlap_intervals[-1]+1:]
    
        return new_list

        