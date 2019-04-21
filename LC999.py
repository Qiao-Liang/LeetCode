class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0

        for r in range(8):
            for c in range(8):
                if board[r][c] == "R":
                    temp_r = r - 1

                    while temp_r > -1:
                        if board[temp_r][c] == '.':
                            temp_r -= 1
                        else :
                            res += board[temp_r][c] == 'p'
                            break

                    temp_r = r + 1

                    while temp_r < 8:
                        if board[temp_r][c] == '.':
                            temp_r += 1
                        else :
                            res += board[temp_r][c] == 'p'
                            break

                    temp_c = c - 1

                    while temp_c > -1:
                        if board[r][temp_c] == '.':
                            temp_c -= 1
                        else:
                            res += board[r][temp_c] == 'p'
                            break

                    temp_c = c + 1

                    while temp_c < 8:
                        if board[r][temp_c] == '.':
                            temp_c += 1
                        else:
                            res += board[r][temp_c] == 'p'
                            break

                    return res

        return 0


sol = Solution()
# board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(sol.numRookCaptures(board))
