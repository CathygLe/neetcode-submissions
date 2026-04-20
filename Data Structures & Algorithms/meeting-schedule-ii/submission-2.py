"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # hint: check how many meetings start before a meeting ends
        # hint: separate arrays for start and end times needed 
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        # position at start and position at end
        s, e = 0, 0 

        while s < len(intervals):
            # if starting before an end
            if start[s] < end[e]:
                s += 1
                count += 1
            # if ending before a next start
            else:
                e +=1
                count -= 1
            res = max(res, count)
        
        return res
        