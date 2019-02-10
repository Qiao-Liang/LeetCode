class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_x = m
        min_y = n

        for x, y in ops:
            min_x = min(x, min_x)
            min_y = min(y, min_y)

        return min_x * min_y


sol = Solution()
m = 3
n = 3
ops = [[2,2],[3,3]]
# m = 18
# n = 3
# ops = [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]
print(sol.maxCount(m, n, ops))
        