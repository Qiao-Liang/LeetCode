class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        row, col = 0, 0
        max_row, max_col = len(matrix), len(matrix[0])
        dirts = ((-1, 1), (1, -1))
        dirt = dirts[0]
        result = []

        while row < max_row and col < max_col:
            result.append(matrix[row][col])

            if row + dirt[0] < 0 or col + dirt[1] == max_col:
                if col + dirt[1] == max_col:
                    row += 1
                else:
                    col += 1

                dirt = dirts[1]
            elif col + dirt[1] < 0 or row + dirt[0] == max_row:
                if row + dirt[0] == max_row:
                    col += 1
                else:
                    row += 1

                dirt = dirts[0]
            else:
                row, col = row + dirt[0], col + dirt[1]

        return result

sol = Solution()
# m = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
m = [[]]
# m = [[1, 2, 3, 4], [5, 6, 7, 8]]

print(sol.findDiagonalOrder(m))
