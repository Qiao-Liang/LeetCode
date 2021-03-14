class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_grid = len(grid)
        memo = [[[None] * len_grid for _ in range(len_grid)] for _ in range(len_grid)]

        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2

            if r1 == len_grid or r2 == len_grid or c1 == len_grid or c2 == len_grid or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            elif r1 == c1 == len_grid - 1:
                return grid[r1][c1]
            elif memo[r1][c1][c2]:
                return memo[r1][c1][c2]
            else:
                res = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                res += max(dp(r1, c1 + 1, c2), dp(r1 + 1, c1, c2 + 1), dp(r1, c1 + 1, c2), dp(r1 + 1, c1, c2))
            
            memo[r1][c1][c2] = res
            return res
