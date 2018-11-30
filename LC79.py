class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False

        rows = len(board)
        cols = len(board[0])
        curr = 0
        len_word = len(word)

        def dfs(r, c, board, visited, word, idx):
            visited[r][c] = True

            if idx == len(word):
                return True

            if r > 0 and not visited[r - 1][c] and board[r - 1][c] == word[idx] and dfs(r - 1, c, board, visited, word, idx + 1):
                return True

            if r < len(board) - 1 and not visited[r + 1][c] and board[r + 1][c] == word[idx] and dfs(r + 1, c, board, visited, word, idx + 1):
                return True

            if c > 0 and not visited[r][c - 1] and board[r][c - 1] == word[idx] and dfs(r, c - 1, board, visited, word, idx + 1):
                return True

            if c < len(board[0]) - 1 and not visited[r][c + 1] and board[r][c + 1] == word[idx] and dfs(r, c + 1, board, visited, word, idx + 1):
                return True
            
            visited[r][c] = False

            return False

        for r in xrange(rows):
            for c in xrange(cols):
                if board[r][c] == word[0]:
                    visited = [[False] * cols for _ in xrange(rows)]

                    if dfs(r, c, board, visited, word, 1):
                        return True

        return False


sol = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "SEE"

print sol.exist(board, word)
