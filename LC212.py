from collections import defaultdict

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words or not board:
            return []

        word_dic = defaultdict(list)
        rows = len(board)
        cols = len(board[0])
        res = set([])

        for word in words:
            word_dic[word[0]].append(word)

        def dfs(r, c, idx, target, visited):
            if idx == len(target):
                return True

            res = False

            if r + 1 < rows and (r + 1, c) not in visited and board[r + 1][c] == target[idx]:
                visited.add((r + 1, c))
                res = res or dfs(r + 1, c, idx + 1, target, visited)
                visited.remove((r + 1, c))

            if r - 1 > -1 and (r - 1, c) not in visited and board[r - 1][c] == target[idx]:
                visited.add((r - 1, c))
                res = res or dfs(r - 1, c, idx + 1, target, visited)
                visited.remove((r - 1, c))

            if c + 1 < cols and (r, c + 1) not in visited and board[r][c + 1] == target[idx]:
                visited.add((r, c + 1))
                res = res or dfs(r, c + 1, idx + 1, target, visited)
                visited.remove((r, c + 1))

            if c - 1 > -1 and (r, c - 1) not in visited and board[r][c - 1] == target[idx]:
                visited.add((r, c - 1))
                res = res or dfs(r, c - 1, idx + 1, target, visited)
                visited.remove((r, c - 1))

            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in word_dic:
                    for word in word_dic[board[r][c]]:
                        if dfs(r, c, 1, word, set([(r, c)])):
                            res.add(word)

        return list(res)


sol = Solution()
# words = ["oath","pea","eat","rain"]
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
board = [["a","a"]]
words = ["aaa"]
# board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["b","c","d","e"],["f","g","h","i"],["j","k","l","m"],["n","o","p","q"],["r","s","t","u"],["v","w","x","y"],["z","z","z","z"]]
print(sol.findWords(board, words))
