class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row_bound = len(matrix)
        col_bound = len(matrix[0])

        def bfs(row, col):
            queue = [(row, col)]
            dist = 0
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                dist += 1
                count = len(queue)
                while count > 0:
                    curr = queue.pop(0)

                    for dir in dirs:
                        r,  c = curr[0] + dir[0], curr[1] + dir[1]

                        if 0 <= r < row_bound and 0 <= c < col_bound:
                            if matrix[r][c] == 0:
                                return dist
                            else:
                                queue.append((r, c))
                        else:
                            continue
                    
                    count -= 1
        
        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                if col != 0:
                    matrix[r][c] = bfs(r, c)
        
        return matrix

# sol = Solution()
# matrix = [[0,0,0],[0,1,0],[1,1,1]]
# result = sol.updateMatrix(matrix)
# print(result)
