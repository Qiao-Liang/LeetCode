class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        path = [[0] * cols for i in range(rows)]

        if obstacleGrid[-1][-1] == 0:
            path[-1][-1] = 1
        else:
            path[-1][-1] = 0

        for idx in range(rows - 2, -1, -1):
            if obstacleGrid[idx][-1] == 0:
                path[idx][-1] = path[idx + 1][-1]
            else:
                path[idx][-1] = 0
        for idx in range(cols - 2, -1, -1):
            if obstacleGrid[-1][idx] == 0:
                path[-1][idx] = path[-1][idx + 1]
            else:
                path[-1][idx] = 0

        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    path[row][col] = 0
                else:
                    path[row][col] = path[row + 1][col] + path[row][col + 1]
        
        return path[0][0]


# m = [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
m = [[0, 1]]
sol = Solution()
print(sol.uniquePathsWithObstacles(m))
