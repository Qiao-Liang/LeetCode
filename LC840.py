class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_bound = len(grid) - 2
        col_bound = len(grid[0]) - 2
        res = 0

        for r in range(row_bound):
            for c in range(col_bound):
                temp_set = []
                temp_set.extend(grid[r][c: c + 3])
                temp_set.extend(grid[r + 1][c: c + 3])
                temp_set.extend(grid[r + 2][c: c + 3])

                if min(temp_set) < 1 or max(temp_set) > 9 or len(set(temp_set)) < 9:
                    continue

                temp = sum(grid[r][c: c + 3])

                if sum(grid[r + 1][c: c + 3]) != temp or sum(grid[r + 2][c: c + 3]) != temp:
                    continue

                if not grid[r][c] + grid[r + 1][c] + grid[r + 2][c] == grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] == grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2]:
                    continue

                if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]:
                    continue

                res += 1

        return res


sol = Solution()
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# grid = [[5,5,5], [5,5,5], [5,5,5]]
print(sol.numMagicSquaresInside(grid))
