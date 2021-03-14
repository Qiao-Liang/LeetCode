class Solution:
    def maxDistance(self, grid) -> int:
        n = len(grid)
        queue = [(r, c) for r in range(n) for c in range(n) if grid[r][c]]

        if not queue or len(queue) == n ** 2:
            return -1

        res = -1

        while queue:
            temp = []

            for r, c in queue:
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if -1 < nr < n and -1 < nc < n and grid[nr][nc] != 1:
                        grid[nr][nc] = 1
                        temp.append((nr, nc))
            
            queue = temp
            res += 1

        return res


        # rows = len(grid)
        # cols = len(grid[0])
        # res = 0
        
        # def bfs(r, c):
        #     queue = [(r, c)]
        #     visited = set([(r, c)])
            
        #     while queue:
        #         temp = []
                
        #         for xr, xc in queue:
        #             for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        #                 nr, nc = xr + dr, xc + dc
                        
        #                 if -1 < nr < rows and -1 < nc < cols:
        #                     if grid[nr][nc] == 1:
        #                         return abs(nr - r) + abs(nc - c)
        #                     elif (nr, nc) not in visited:
        #                         visited.add((nr, nc))
        #                         temp.append((nr, nc))
                            
        #         queue = temp
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 0:
        #             temp = bfs(r, c)
        #             res = max(res, temp if temp else 0)
        
        # return res if res else -1


sol = Solution()
# g = [[0,0,0],[0,0,0],[0,0,0]]
# g = [[1,1,1],[1,1,1],[1,1,1]]
g = [[1,0,1],[0,0,0],[1,0,1]]
# g = [[1,0,0],[0,0,0],[0,0,0]]
print(sol.maxDistance(g))
