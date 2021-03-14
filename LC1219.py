class Solution:
    def getMaximumGold(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c, visited):
            temp = []
            v = grid[r][c]

            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc

                if -1 < nr < rows and -1 < nc < cols and grid[nr][nc] != 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    temp.append(dfs(nr, nc, visited))
                    visited.remove((nr, nc))
            
            return (v + max(temp)) if temp else v

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    res = max(res, dfs(r, c, set([(r, c)])))
        
        return res


sol = Solution()
# m = [
#     [0,6,0],
#     [5,8,7],
#     [0,9,0]
# ]
# m = [
#     [1,0,7],
#     [2,0,6],
#     [3,4,5],
#     [0,3,0],
#     [9,0,20]
# ]
# m = [[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]
m = [[0,0,19,5,8],[11,20,14,1,0],[0,0,1,1,1],[0,2,0,2,0]]
print(sol.getMaximumGold(m))
