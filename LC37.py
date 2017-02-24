class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.recurse()
        
    def recurse(self):
        row = -1
        col = -1
        
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '.':
                    row = r
                    col = c
                    break
        
        # Base case
        if row == -1 and col == -1:
            return True
        
        num_set = self.get_acceptable_num(row, col)
        if len(num_set) == 0:
            return False
        else:
            for num in num_set:
                self.board[row][col] = num
                if self.recurse():
                    return True
                
                self.board[row][col] = '.'
        
        return False

    def get_acceptable_num(self, row, col):
        num_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # Check columns
        for c in self.board[row]:
            if c in num_set:
                num_set.remove(c)
        
        # Check rows
        for r in range(9):
            num = self.board[r][col]
            if num in num_set:
                num_set.remove(num)

        # Check 3*3 section
        row_start = int(row / 3) * 3
        col_start = int(col / 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                num = self.board[r][c]
                if num in num_set:
                    num_set.remove(num)
        
        return num_set