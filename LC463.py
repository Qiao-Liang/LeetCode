class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        unvisited = [[True] * cols for _ in xrange(rows)]

        for row in xrange(rows):
            for col in xrange(cols):
                if grid[row][col] == 1:
                    queue = [(row, col)]
                    unvisited[row][col] = False

                    while queue:
                        r, c = queue.pop(0)
                        grid[r][c] = 2

                        if r > 0:
                            if grid[r - 1][c] == 0:
                                res += 1
                            elif grid[r - 1][c] == 1 and unvisited[r - 1][c]:
                                unvisited[r - 1][c] = False
                                queue.append((r - 1, c))
                        else:
                            res += 1

                        if r < rows - 1:
                            if grid[r + 1][c] == 0:
                                res += 1
                            elif grid[r + 1][c] == 1 and unvisited[r + 1][c]:
                                unvisited[r + 1][c] = False
                                queue.append((r + 1, c))
                        else:
                            res += 1

                        if c > 0:
                            if grid[r][c - 1] == 0:
                                res += 1
                            elif grid[r][c - 1] == 1 and unvisited[r][c - 1]:
                                unvisited[r][c - 1] = False
                                queue.append((r, c - 1))
                        else:
                            res += 1

                        if c < cols - 1:
                            if grid[r][c + 1] == 0:
                                res += 1
                            elif grid[r][c + 1] == 1 and unvisited[r][c + 1]:
                                unvisited[r][c + 1] = False
                                queue.append((r, c + 1))
                        else:
                            res += 1

        return res

    def islandPerimeter2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        p = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    p = p+4
                    if m != 0 and grid[m-1][n] == 1:
                        p = p-1
                    if m != M-1 and grid[m+1][n] == 1:
                        p = p-1
                    if n != 0 and grid[m][n-1] == 1:
                        p = p-1
                    if n != N-1 and grid[m][n+1] == 1:
                        p = p-1
        return p


sol = Solution()
# grid = [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# grid = [[1, 1], [1, 1]]
grid = [[0, 1]]
print sol.islandPerimeter(grid)
        