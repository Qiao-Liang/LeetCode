class Solution:
    def minimumJumps(self, forbidden, a: int, b: int, x: int) -> int:
        q = [(0, True)]
        res = 0
        
        while q:
            temp = set()
            
            for n, cb in q:
                if n == x:
                    return res
                
                t1 = n + a
                t2 = n - b
                
                if t1 not in forbidden:
                    temp.add((t1, True))
                
                if cb and t2 not in forbidden:
                    temp.add((t2, False))
            
            res += 1
            q = list(temp)
            
        return -1


sol = Solution()
p = [[8,3,16,6,12,20],15,13,11]
print(sol.minimumJumps(*p))
