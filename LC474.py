from collections import Counter

class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            c = Counter(s)
            c0, c1 = c['0'], c['1']
            
            for i0 in range(m, c0 - 1, -1):
                for i1 in range(n, c1 - 1, -1):
                    dp[i0][i1] = max(dp[i0][i1], dp[i0 - c0][i1 - c1] + 1)
        
        return dp[-1][-1]


sol = Solution()
p = [["10","0001","111001","1","0"], 5, 3]
print(sol.findMaxForm(*p))
