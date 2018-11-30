class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []

        while top < bottom and left < right:
            for c in range(left, right + 1):
                res.append(matrix[top][c])

            for r in range(top + 1, bottom):
                res.append(matrix[r][right])
            
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])

            for r in range(bottom - 1, top, -1):
                res.append(matrix[r][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        if top == bottom:
            res.extend(matrix[top][left: right + 1])
        elif left == right:
            res.extend([row[left] for row in matrix[top: bottom + 1]])

        return res


        # if not matrix:
        #     return []

        # top = 0
        # bottom = len(matrix) - 1
        # left = 0
        # right = len(matrix[0]) - 1
        # result = []

        # while top <= bottom and left <= right:
        #     left_list, right_list = [], []

        #     for idx in range(top + 1, bottom):
        #         right_list.append(matrix[idx][right])
        #         if left != right:
        #             left_list.append(matrix[idx][left])

        #     result.extend(matrix[top][left:right + 1])
        #     result.extend(right_list)
        #     if top != bottom:
        #         result.extend(matrix[bottom][left:right + 1][::-1])
        #     if left != right:
        #         result.extend(left_list[::-1])

        #     top += 1
        #     bottom -= 1
        #     left += 1
        #     right -= 1

        # return result

sol = Solution()
# m = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# m = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
#     [7, 8]
# ]
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ]
# m = [[7], [9], [6]]

# m = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]

# m = [[3], [2]]

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

print(sol.spiralOrder(m))
