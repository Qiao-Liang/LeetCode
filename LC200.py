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

    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dis_set = {}
        
        def find(x):
            if x != dis_set[x]:
                dis_set[x] = find(dis_set[x])
                
            return dis_set[x]
        
        def union(x, y):
            dis_set[find(x)] = dis_set[find(y)]
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dis_set[r, c] = (r, c)
                    
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nr = r + dr
                        nc = c + dc
                        
                        if (nr, nc) in dis_set:
                            union((r, c), (nr, nc))

        for key in dis_set:
            find(key)
        
        return len(set(dis_set.values()))


sol = Solution()
grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]
print(sol.numIslands(grid))
