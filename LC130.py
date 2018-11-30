class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        border_cells = []
        rows = len(board)
        cols = len(board[0])
        row_bound = rows - 1
        col_bound = cols - 1

        for idx, val in enumerate(board[0]):
            if val == "O":
                border_cells.append((0, idx))

        for idx, val in enumerate(board[-1]):
            if val == "O":
                border_cells.append((row_bound, idx))

        for idx, row in enumerate(board):
            if row[0] == "O":
                border_cells.append((idx, 0))

            if row[-1] == "O":
                border_cells.append((idx, col_bound))

        for cell in border_cells:
            if board[cell[0]][cell[1]] == "O":
                queue = [cell]
                board[cell[0]][cell[1]] = "Y"

                while queue:
                    r, c = queue.pop(0)

                    if r > 0 and board[r - 1][c] == "O":
                        board[r - 1][c] = "Y"
                        queue.append((r - 1, c))

                    if r < row_bound and board[r + 1][c] == "O":
                        board[r + 1][c] = "Y"
                        queue.append((r + 1, c))

                    if c > 0 and board[r][c - 1] == "O":
                        board[r][c - 1] = "Y"
                        queue.append((r, c - 1))

                    if c < col_bound and board[r][c + 1] == "O":
                        board[r][c + 1] = "Y"
                        queue.append((r, c + 1))

        for r in xrange(rows):
            for c in xrange(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "Y":
                    board[r][c] = "O"

        print board


sol = Solution()
# board = [
#     ['X', 'X', 'X', 'X'],
#     ['X', 'O', 'O', 'X'],
#     ['X', 'X', 'O', 'X'],
#     ['X', 'O', 'X', 'X']
# ]
# board = [
#     ['O', 'O'],
#     ['O', 'O']
# ]

board = [
    ["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],
    ["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],
    ["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],
    ["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],
    ["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],
    ["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],
    ["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],
    ["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],
    ["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],
    ["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],
    ["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],
    ["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],
    ["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],
    ["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],
    ["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],
    ["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],
    ["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],
    ["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],
    ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],
    ["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]]

from time import time
t = time()
sol.solve(board)
print time() - t
        