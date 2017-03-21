class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False

        col = len(matrix[0])

        mid_row = row // 2
        mid_col = col // 2
        mid_val = matrix[mid_row][mid_col]

        if target == mid_val:
            return True
        elif target < mid_val:
            new_matrix = []
            for i in range(mid_row):
                new_matrix.append(matrix[i][:mid_col])

            return self.searchMatrix(new_matrix, target)
        else:
            new_matrix_upper = []
            new_matrix_lower = []

            for i in range(mid_row + 1):
                new_matrix_upper.append(matrix[i][mid_col + 1:])
            
            for i in range(mid_row + 1, row):
                new_matrix_lower.append(matrix[i][:])

            return self.searchMatrix(new_matrix_upper, target) or self.searchMatrix(new_matrix_lower, target)



    
    # def binarySearch(self, array, target):
    #     if len(array) == 0:
    #         return False

    #     mid = len(array) // 2

    #     if target == array[mid]:
    #         return True
    #     elif target < array[mid]:
    #         return self.binarySearch(array[:mid], target)
    #     else:
    #         return self.binarySearch(array[mid + 1:], target)
