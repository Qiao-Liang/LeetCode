class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        lx, ly = points[0]
        res = 0
        
        for x, y in points[1:]:
            tx = abs(lx - x)
            ty = abs(ly - y)
            
            if tx > ty:
                res += tx
            elif tx < ty:
                res += ty
            else:
                res += tx
                
            lx = x
            ly = y
            
        return res


sol = Solution()
p = [[3,2],[-2,2]]
print(sol.minTimeToVisitAllPoints(p))
