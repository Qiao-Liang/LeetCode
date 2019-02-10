class Solution:
    def surfaceArea(self, grid):
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
            for cube in row:
                if cube:
                    res += 2 + 4 * cube

        for r in range(rows):
            for c in range(cols):
                temp = grid[r][c]

                if r - 1 > -1:
                    res -= min(temp, grid[r - 1][c])

                if r + 1 < rows:
                    res -= min(temp, grid[r + 1][c])

                if c - 1 > -1:
                    res -= min(temp, grid[r][c - 1])

                if c + 1 < cols:
                    res -= min(temp, grid[r][c + 1])

        return res

        # for r_idx, row in enumerate(grid):
        #     for c_idx, count in enumerate(row):
        #         if count > 0:
        #             res += 1

        #         if r_idx - 1 > -1 and grid[r_idx - 1][c_idx] > count:
        #             inside += grid[r_idx - 1][c_idx] - count

        #         if r_idx + 1 < rows and grid[r_idx + 1][c_idx] > count:
        #             inside += grid[r_idx + 1][c_idx] - count

        #         if c_idx - 1 > -1 and grid[r_idx][c_idx - 1] > count:
        #             inside += grid[r_idx][c_idx - 1] - count

        #         if c_idx + 1 < cols and grid[r_idx][c_idx + 1] > count:
        #             inside += grid[r_idx][c_idx + 1] - count

        # for x in grid:
        #     res += max(x)

        # for y in range(cols):
        #     res += max([row[y] for row in grid])

        # return res * 2 + inside


sol = Solution()
# g = [[2]]
# g = [[1,2],[3,4]]
# g = [[1,1,1],[1,0,1],[1,1,1]]
# g = [[2,2,2],[2,1,2],[2,2,2]]
g = [[3,3,3],[3,4,5],[5,0,4]]
# g = [[1,0],[0,2]]
print(sol.surfaceArea(g))
        