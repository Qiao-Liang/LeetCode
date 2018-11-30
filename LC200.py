class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for row in xrange(rows):
            for col in xrange(cols):
                if grid[row][col] == '1':
                    res += 1
                    queue = [(row, col)]

                    while queue:
                        r, c = queue.pop(0)
                        grid[r][c] = '0'

                        if r > 0 and grid[r - 1][c] == '1':
                            grid[r - 1][c] = '0'
                            queue.append((r - 1, c))

                        if r < rows - 1 and grid[r + 1][c] == '1':
                            grid[r + 1][c] = '0'
                            queue.append((r + 1, c))

                        if c > 0 and grid[r][c - 1] == '1':
                            grid[r][c - 1] = '0'
                            queue.append((r, c - 1))

                        if c < cols - 1 and grid[r][c + 1] == '1':
                            grid[r][c + 1] = '0'
                            queue.append((r, c + 1))
        
        return res


sol = Solution()
grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]
print sol.numIslands(grid)
