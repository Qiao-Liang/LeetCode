class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [[0] * (n + 1) for _ in range(n + 1)]

        for lo in range(n - 1, 0, -1):
            for hi in range(lo + 1, n + 1):
                memo[lo][hi] = min([pivot + max(memo[lo][pivot - 1], memo[pivot + 1][hi]) for pivot in range(lo, hi)])
        
        return memo[1][-1]


sol = Solution()
print(sol.getMoneyAmount(10))
