class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0:
            return False

        for row in matrix:
            if target < row[0]:
                return False
            elif target > row[-1]:
                continue
            else:
                left = 0
                right = len(row) - 1

                while left <= right:
                    mid = (left + right) // 2
                    
                    if row[mid] < target:
                        left = mid + 1
                    elif row[mid] > target:
                        right = mid - 1
                    else:
                        return True

        return False


sol = Solution()
# matrix = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# matrix = [[-1, 3]]
# matrix = [[5], [6]]

# matrix = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]]

matrix = [
    [3,3,8,13,13,18],
    [4,5,11,13,18,20],
    [9,9,14,15,23,23],
    [13,18,22,22,25,27],
    [18,22,23,28,30,33],
    [21,25,28,30,35,35],
    [24,25,33,36,37,40]]

print(sol.searchMatrix(matrix, 21))
