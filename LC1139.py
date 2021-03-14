class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        rs = len(grid)
        cs = len(grid[0])
        
        for r in range(rs):
            for c in range(cs):
                if grid[r][c] == 1:
                    tr = r
                    tc = c
                    
                    while tr < rs and tc < cs and grid[tr][c] == grid[r][tc] == 1:
                        tr += 1
                        tc += 1
                        
                    tr -= 1
                    tc -= 1
                    is_square = True
                    
                    for i in range(1, tr - r + 1):
                        if grid[tr][c + i] == 0 or grid[r + i][tc] == 0:
                            is_square = False
                            break
                            
                    if is_square:
                        res = max(res, (tr - r + 1) ** 2)
        
        return res


sol = Solution()

