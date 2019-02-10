class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0

        rows = len(board)
        cols = len(board[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    res += 1
                    board[r][c] = '.'
                    temp_r = r + 1
                    temp_c = c + 1

                    while temp_r < rows and board[temp_r][c] == 'X':
                        board[temp_r][c] = '.'
                        temp_r += 1

                    while temp_c < cols and board[r][temp_c] == 'X':
                        board[r][temp_c] = '.'
                        temp_c += 1

        return res


sol = Solution()
board = [
    ['X','.','.','X'],
    ['.','.','.','X'],
    ['.','.','.','X']
]

print(sol.countBattleships(board))
        