class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.accu_matrix = [row[:] for row in matrix]

        for row in self.accu_matrix:
            for idx in range(1, len(row)):
                row[idx] += row[idx - 1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0

        for row in self.accu_matrix[row1: row2 + 1]:
            res += row[col2] - (row[col1 - 1] if col1 > 0 else 0)

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

matrix = [[-1]]

num_matrix = NumMatrix(matrix)
# print(num_matrix.sumRegion(2, 1, 4, 3))
# print(num_matrix.sumRegion(1, 1, 2, 2))
print(num_matrix.sumRegion(0, 0, 0, 0))
