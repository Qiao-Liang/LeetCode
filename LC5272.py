class Solution:
    def countServers(self, grid) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cnt = 1
                    grid[r][c] = 0
                    queue = [(r, c)]
                    
                    while queue:
                        temp = []
                        
                        for cr, cc in queue:
                            for tr in range(rows):
                                if grid[tr][cc] == 1:
                                    cnt += 1
                                    grid[tr][cc] = 0
                                    temp.append((tr, cc))
                                    
                            for tc in range(cols):
                                if grid[cr][tc] == 1:
                                    cnt += 1
                                    grid[cr][tc] = 0
                                    temp.append((cr, tc))
                                    
                        queue = temp
                        
                    if cnt > 1:
                        res += cnt
        
        return res


sol = Solution()
p = [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]
print(sol.countServers(p))
