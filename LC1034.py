class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        target = grid[r0][c0]
        queue = [(r0, c0)]
        direc = [1, 0, -1, 0, 1]
        rows = len(grid)
        cols = len(grid[0])
        visited = set([(r0, c0)])
        borders = []
            
        for r, c in queue:
            is_border = False

            for d in range(4):
                next_r = r + direc[d]
                next_c = c + direc[d + 1]
                
                if -1 < next_r < rows and -1 < next_c < cols and grid[next_r][next_c] == target: 
                    if (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        queue.append((next_r, next_c))
                else:
                    is_border = True
        
            if is_border:
                borders.append((r, c))

        for r, c in borders:
            grid[r][c] = color
        
        return grid


sol = Solution()
# grid = [[1,1],[1,2]]
# r0 = 0
# c0 = 0
# color = 3
# params = [
#     [[1,1,1],[1,1,1],[1,1,1]],
# 1,
# 1,
# 2]
params = [
    [[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]],
    1,
    3,
    1
]
print(sol.colorBorder(*params))
