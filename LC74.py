class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] or target is None:
            return False

        def bin_search(target, arr):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) / 2

                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return target

            return (left, right)

        res = bin_search(target, [row[0] for row in matrix])

        if type(res) == int:
            return True
        
        res = bin_search(target, matrix[min(res)])

        return type(res) == int


sol = Solution()
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13

matrix = [[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]]
target = 0
print sol.searchMatrix(matrix, target)
        