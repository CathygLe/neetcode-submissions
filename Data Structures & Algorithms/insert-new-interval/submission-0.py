class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # newInterval = [start, end]

            # check if it goes before i (compare new end < start)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # append the rest
                return res + intervals[i:]
            
            # check if it goes after i (compare start > end)
            elif newInterval[0] > intervals[i][1]: 
                res.append(intervals[i])
            
            #overlapping
            else: 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval)
        return res 

        