class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for row in grid:
            for count in row:
                if count > 0:
                    res += 1

        for x in grid:
            res += max(x)

        for y in range(cols):
            res += max([row[y] for row in grid])

        return res
        

sol = Solution()
# grid = [[1,2],[3,4]]
# grid = [[1,1,1],[1,0,1],[1,1,1]]
grid = [[2,2,2],[2,1,2],[2,2,2]]
print(sol.projectionArea(grid))
