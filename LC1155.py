class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def dfs(i, t):
            if i == 0:
                return 1 if t == 0 else 0
            elif (i, t) in memo:
                return memo[(i, t)]
            else:
                res = 0

                for n in range(1, f + 1):
                    if n <= t:
                        res += dfs(i - 1, t - n)
                
                memo[(i, t)] = res
                return res
        
        return dfs(d, target) % (10 ** 9 + 7)


sol = Solution()
# p = [1, 6, 3]
# p = [2, 6, 7]
# p = [2, 5, 10]
# p = [1,2,3]
p = [30, 30, 500]
print(sol.numRollsToTarget(*p))
