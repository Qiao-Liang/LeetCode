class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.queens = [-1] * n

        def is_valid(row, col):
            if col in self.queens:
                return False

            temp_row = row - 1
            temp_col = col - 1
            while temp_row > -1 and temp_col > -1:
                if self.queens[temp_row] == temp_col:
                    return False

                temp_row -= 1
                temp_col -= 1

            temp_row = row + 1
            temp_col = col - 1
            while temp_row < n and temp_col > -1:
                if self.queens[temp_row] == temp_col:
                    return False

                temp_row += 1
                temp_col -= 1

            temp_row = row - 1
            temp_col = col + 1
            while temp_row > -1 and temp_col < n:
                if self.queens[temp_row] == temp_col:
                    return False

                temp_row -= 1
                temp_col += 1

            temp_row = row + 1
            temp_col = col + 1
            while temp_row < n and temp_col < n:
                if self.queens[temp_row] == temp_col:
                    return False

                temp_row += 1
                temp_col += 1

            return True

        def recurse(row):
            if row == n:
                temp = [["."] * n for idx in xrange(n)]

                for idx in xrange(n):
                    temp[idx][self.queens[idx]] = "Q"

                self.result.append(map(lambda x: ''.join(x), temp))

                return False

            for col in xrange(n):
                if is_valid(row, col):
                    self.queens[row] = col

                    if recurse(row + 1):
                        return True
                    else:
                        self.queens[row] = -1
                        continue

            return False

        recurse(0)

        return self.result


sol = Solution()
temps = sol.solveNQueens(4)

# for temp in temps:
#     for row in temp:
#         print row
print temps
