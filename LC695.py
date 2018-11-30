class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        row_count = len(grid)
        col_count = len(grid[0])

        for row in xrange(row_count):
            for col in xrange(col_count):
                if grid[row][col] == 1:
                    temp_area = 0
                    queue = [(row, col)]
                    grid[row][col] = 0

                    while queue:
                        curr_row, curr_col = queue.pop(0)
                        temp_area += 1

                        if curr_row > 0 and grid[curr_row - 1][curr_col] == 1:
                            grid[curr_row - 1][curr_col] = 0
                            queue.append((curr_row - 1, curr_col))

                        if curr_row < row_count - 1 and grid[curr_row + 1][curr_col] == 1:
                            grid[curr_row + 1][curr_col] = 0
                            queue.append((curr_row + 1, curr_col))

                        if curr_col > 0 and grid[curr_row][curr_col - 1] == 1:
                            grid[curr_row][curr_col - 1] = 0
                            queue.append((curr_row, curr_col - 1))

                        if curr_col < col_count - 1 and grid[curr_row][curr_col + 1] == 1:
                            grid[curr_row][curr_col + 1] = 0
                            queue.append((curr_row, curr_col + 1))

                    max_area = max(max_area, temp_area)

        return max_area


sol = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# grid = [[0,0,0,0,0,0,0,0]]
# grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print sol.maxAreaOfIsland(grid)
        