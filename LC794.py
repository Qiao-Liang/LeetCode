class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        dic1 = {"X": 0, "O": 0, " ": 0}

        for row in board:
            for ch in row:
                dic1[ch] += 1

        if dic1["X"] - dic1["O"] not in (0, 1):
            return False

        possible_wins = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]]
        ]
                
        dic2 = {"X": 0, "O": 0, " ": 0}

        for win in possible_wins:
            if board[win[0][0]][win[0][1]] == board[win[1][0]][win[1][1]] == board[win[2][0]][win[2][1]]:
                dic2[board[win[0][0]][win[0][1]]] += 1

        return dic2["X"] == dic2["O"] == 0 or (dic2["X"] > 0 and dic2["O"] == 0 and dic1["X"] > dic1["O"]) or (dic2["O"] > 0 and dic2["X"] == 0 and dic1["X"] == dic1["O"])


sol = Solution()
# board = ["XOX", "O O", "XOX"]
# board = ["XXX", "   ", "OOO"]
# board = ["XOX", " X ", "   "]
board = ["O  ", "   ", "   "]
# board = ["XXX","OOX","OOX"]
# board = ["XXX","XOO","O  "]
print(sol.validTicTacToe(board))
        