class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        queue = []
        fresh_count = 0
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        while True:
            temp_queue = []

            for r, c in queue:
                if r + 1 < rows and grid[r + 1][c] == 1:
                    temp_queue.append((r + 1, c))
                    grid[r + 1][c] = 2
                    fresh_count -= 1

                if r - 1 > -1 and grid[r - 1][c] == 1:
                    temp_queue.append((r - 1, c))
                    grid[r - 1][c] = 2
                    fresh_count -= 1

                if c + 1 < cols and grid[r][c + 1] == 1:
                    temp_queue.append((r, c + 1))
                    grid[r][c + 1] = 2
                    fresh_count -= 1

                if c - 1 > -1 and grid[r][c - 1] == 1:
                    temp_queue.append((r, c - 1))
                    grid[r][c - 1] = 2
                    fresh_count -= 1

            queue = temp_queue

            if queue:
                res += 1
            else:
                break

        return -1 if fresh_count else res


sol = Solution()
g = [[2,1,1],[1,1,0],[0,1,1]]
# g = [[2,1,1],[0,1,1],[1,0,1]]
print(sol.orangesRotting(g))
