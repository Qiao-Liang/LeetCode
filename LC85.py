class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        acc_row = [[int(n) for n in matrix[0]]]
        acc_col = []
        row_max = 1 if matrix[0][0] == "1" else 0
        col_max = row_max
        rec_max = 0
        
        for row in matrix:
            temp = [int(row[0])]

            for col_idx in range(1, cols):
                if row[col_idx] == "0":
                    temp.append(0)
                else:
                    temp.append(int(row[col_idx]) + temp[-1])

                if temp[-1] > col_max:
                    col_max = temp[-1]
            
            acc_col.append(temp)

        for row_idx in range(1, rows):
            temp = acc_row[row_idx - 1][:]

            for col_idx in range(0, cols):
                if matrix[row_idx][col_idx] == "0":
                    temp[col_idx] = 0
                else:
                    temp[col_idx] += int(matrix[row_idx][col_idx])

                    if temp[col_idx] > row_max:
                        row_max = temp[col_idx]

            acc_row.append(temp)

        for row_idx in range(1, rows):
            for col_idx in range(1, cols):
                if matrix[row_idx][col_idx] == matrix[row_idx - 1][col_idx] == matrix[row_idx][col_idx - 1] == matrix[row_idx - 1][col_idx - 1] == "1":
                    temp_row = row_idx
                    temp_col = col_idx
                    min_row = acc_row[row_idx][col_idx]
                    min_col = acc_col[row_idx][col_idx]

                    if row_idx == 4 and col_idx == 3:
                        print min_row, min_col

                    while temp_row > -1 and matrix[temp_row][col_idx] == "1" and matrix[temp_row][col_idx - 1] == "1":
                        if acc_col[temp_row][col_idx] < min_col:
                            min_col = acc_col[temp_row][col_idx]

                        temp_row -= 1

                    while temp_col > -1 and matrix[row_idx][temp_col] == "1" and matrix[row_idx - 1][temp_col] == "1":
                        if acc_row[row_idx][temp_col] < min_row:
                            min_row = acc_row[row_idx][temp_col]

                        temp_col -= 1

                    if row_idx == 4 and col_idx == 3:
                        print min_row, min_col
                    
                    rec_temp = min_row * min_col
                    if rec_temp > rec_max:
                        rec_max = rec_temp

        return max(row_max, col_max, rec_max)


sol = Solution()

m = [["0","1","1","0","1"],
     ["1","1","0","1","0"],
     ["0","1","1","1","0"],
     ["1","1","1","1","0"],
     ["1","1","1","1","1"],
     ["0","0","0","0","0"]]

# m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(sol.maximalRectangle(m))
