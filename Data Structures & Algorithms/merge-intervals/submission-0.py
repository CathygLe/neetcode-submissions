class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
                        # for each element i, get i[0] (start)
        intervals.sort(key = lambda i: i[0])
        # edge case only 1 element
        output = [intervals[0]]

        for start, end in intervals[1:]:
            
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else: 
                output.append([start,end])
        
        return output

        