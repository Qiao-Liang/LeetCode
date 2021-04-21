class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        row = len(grid)
        col = len(grid[0])
        row_max = [max(r) for r in grid]
        col_max = grid[0][:]
        res = 0
        
        for r in grid[1:]:
            for i, c in enumerate(r):
                col_max[i] = max(col_max[i], c)
                
        for r in range(row):
            for c in range(col):
                res += min(row_max[r], col_max[c]) - grid[r][c]
        
        return res


sol = Solution()
g = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(sol.maxIncreaseKeepingSkyline(g))
