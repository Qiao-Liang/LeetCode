# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals:
            intervals = sorted(intervals, key=lambda i: i.start)
            
            new_intervals = [intervals.pop(0)]
            
            for interval in intervals:
                if new_intervals[-1].end < interval.start:
                    new_intervals.append(interval)
                else:
                    if new_intervals[-1].end < interval.end:
                        new_intervals[-1].end = interval.end
                    
            return new_intervals
        else:
            return []