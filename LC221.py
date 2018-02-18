class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        len_matrix = len(matrix)

        if len_matrix == 1:
            return 1 if '1' in matrix[0] else 0

        len_col = len(matrix[0])
        matrix[0] = map(int, matrix[0])

        for row_idx in range(1, len_matrix):
            matrix[row_idx] = map(int, matrix[row_idx])

            for col_idx in range(1, len_col):
                if matrix[row_idx][col_idx] == 1 and matrix[row_idx - 1][col_idx] > 0 and matrix[row_idx][col_idx - 1] > 0:
                    matrix[row_idx][col_idx] = min(matrix[row_idx - 1][col_idx - 1], matrix[row_idx - 1][col_idx], matrix[row_idx][col_idx - 1]) + 1

        return max(map(max, matrix)) ** 2


sol = Solution()

# m = [
#     ['1', '0', '1', '0', '0'],
#     ['1', '0', '1', '1', '1'],
#     ['1', '1', '1', '1', '1'],
#     ['1', '0', '0', '1', '0']
# ]

# m = [
#     ["1","0","1","0"],
#     ["1","0","1","1"],
#     ["1","0","1","1"],
#     ["1","1","1","1"]
#     ]

# m = [
#     ["0","1","1","0","1"],
#     ["1","1","0","1","0"],
#     ["0","1","1","1","0"],
#     ["1","1","1","1","0"],
#     ["1","1","1","1","1"],
#     ["0","0","0","0","0"]
#     ]

# m = [['0']]

# m = [['1']]

m = [['0', '1'], ['1', '0']]

print(sol.maximalSquare(m))
