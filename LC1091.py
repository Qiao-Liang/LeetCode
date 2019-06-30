class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        res = 0
        queue = [(0, 0)]
        visited = set([])
        bound = len(grid)
        last = bound - 1
        visited.add((0, 0))
        
        def add_node(queue, r, c):
            if -1 < r < bound and -1 < c < bound and grid[r][c] != 1 and (r, c) not in visited:
                queue.append((r, c))
                visited.add((r, c))
        
        while queue:
            temp = []
            res += 1
            
            for r, c in queue:
                if r == last and c == last:
                    return res
                
                add_node(temp, r - 1, c - 1)
                add_node(temp, r - 1, c)
                add_node(temp, r - 1, c + 1)
                add_node(temp, r, c - 1)
                add_node(temp, r, c + 1)
                add_node(temp, r + 1, c - 1)
                add_node(temp, r + 1, c)
                add_node(temp, r + 1, c + 1)
            
            queue = temp
            
        return -1
