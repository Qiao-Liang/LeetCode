class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [1] * m

        while n > 1:
            for idx in range(m - 2, -1, -1):
                path[idx] += path[idx + 1]

            n -= 1

        return path[0]


sol = Solution()
print(sol.uniquePaths(7, 3))
