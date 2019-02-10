class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False

        row_set = [set([]) for _ in range(9)]
        col_set = [set([]) for _ in range(9)]
        group_set = [set([]) for _ in range(9)]
        
        for row, line in enumerate(board):
            for col, val in enumerate(line):
                if val != '.':
                    if val not in row_set[row] and val not in col_set[col] and val not in group_set[(row // 3) * 3 + col // 3]:
                        row_set[row].add(val)
                        col_set[col].add(val)
                        group_set[(row // 3) * 3 + col // 3].add(val)
                    else:
                        return False

        return True


        # if not board:
        #     return False

        # for row in board:
        #     temp = {}

        #     for num in row:
        #         if num != '.':
        #             if num in temp:
        #                 print("1")
        #                 return False
        #             else:
        #                 temp[num] = 1

        # for idx in range(9):
        #     temp = {}

        #     for row in board:
        #         if row[idx] != '.':
        #             if row[idx] in temp:
        #                 print("2")
        #                 return False
        #             else:
        #                 temp[row[idx]] = 1

        # temp = [{}, {}, {}]
        # count = 0
        # for row in board:
        #     if count % 3 == 0:
        #         temp = [{}, {}, {}]
            
        #     start = 0
        #     end = 3

        #     for idx in range(3):
        #         for num in row[start: end]:
        #             if num != '.':
        #                 if num in temp[idx]:
        #                     return False
        #                 else:
        #                     temp[idx][num] = 1

        #         start += 3
        #         end += 3

        #     count += 1

        # return True


sol = Solution()

m = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

print(sol.isValidSudoku(m))
