class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # row_dict = {}
        # col_dict = {}
        
        # for row, row_val in enumerate(matrix):
        #     for col, col_val in enumerate(row_val):
        #         if col_val == 0:
        #             if not row in row_dict:
        #                 row_dict[row] = ''
        #             if not col in col_dict:
        #                 col_dict[col] = ''
        
        # for row in row_dict.keys():
        #     for col in range(len(matrix[row])):
        #         matrix[row][col] = 0
                
        # for col in col_dict.keys():
        #     for row in matrix:
        #         row[col] = 0