class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda n: n[1])
        prv = [points[0]]
        
        for s, e in points[1:]:
            if s > prv[-1][1]:
                prv.append([s, e])
            else:
                prv[-1][0] = max(prv[-1][0], s)
                prv[-1][1] = min(prv[-1][1], e)
                
        return len(prv)
