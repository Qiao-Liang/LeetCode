class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        k_mod = 1000000007
        dp = [[[0] * m for _ in range(n)] for _ in range(N + 1)]
        dirs = [-1, 0, 1, 0, -1]

        for step in range(1, N + 1):
            for r in range(m):
                for c in range(n):
                    for d in range(4):
                        tp_r = r + dirs[d]
                        tp_c = c + dirs[d + 1]

                        if tp_r < 0 or tp_c < 0 or tp_r >= m or tp_c >= n:
                            dp[step][r][c] += 1
                        else:
                            dp[step][r][c] = (dp[step][r][c] + dp[step - 1][tp_r][tp_c]) % k_mod

        return dp[N][i][j]


sol = Solution()
m = 2
n = 2
N = 2
i = 0
j = 0
print(sol.findPaths(m, n, N, i, j))
