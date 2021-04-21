class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda n: n[1])
        res, prv = 0, intervals[0][1]
        
        for s, e in intervals[1:]:
            if s < prv:
                res += 1
            else:
                prv = e
                
        return res
