class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        dist = [[0] * col for i in range(row)]

        dist[0][0] = grid[0][0]
        for idx in range(1, col):
            dist[0][idx] = dist[0][idx - 1] + grid[0][idx]

        for idx in range(1, row):
            dist[idx][0] = dist[idx - 1][0] + grid[idx][0]

        for r in range(1, row):
            for c in range(1, col):
                dist[r][c] = min(dist[r - 1][c], dist[r][c - 1]) + grid[r][c]
        
        return dist[-1][-1]


m = [[1,3,1],
     [1,5,1],
     [4,2,1]]
sol = Solution()
print(sol.minPathSum(m))
