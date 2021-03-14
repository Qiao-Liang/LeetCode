class Solution:
    def dieSimulator(self, n: int, rollMax) -> int:
        res = 6 ** n
        rollMax.sort()
        
        for m in rollMax:
            temp = 0
            
            for c in range(m + 1, n + 1):
                t = n - c
                temp += (t + 1) * (5 ** t)
                
            res -= temp
            
        return res


sol = Solution()
p = [4, [2,1,1,3,3,2]]
print(sol.dieSimulator(*p))
