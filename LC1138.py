class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        len_r = len(board)
        len_t = len(target)
        i = 0
        q = [(0, 0, [])]
        visited = set([(0, 0)])

        while i < len_t:
            for r, c, p in q:
                added = False

                while i < len_t and target[i] == board[r][c]:
                    p.append('!')
                    i += 1
                    added = True
                
                if i == len_t:
                    return ''.join(p)
                
                if added:
                    visited = set([(r, c)])
                    q = [(r, c, p)]
                    break

                for dr, dc, d in ((1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')):
                    tr, tc = r + dr, c + dc

                    if -1 < tr < len_r and -1 < tc < len(board[tr]) and (tr, tc) not in visited:
                        visited.add((tr, tc))
                        q.append((tr, tc, p + [d]))

        
        # def dfs(r, c, visited, path, ti):            
        #     if ti < len_r and -1 < r < len_r and -1 < c < len(board[r]) and (r, c) not in visited:
        #         visited.add((r, c))
        #         added = False
                
        #         while ti < len_r and target[ti] == board[r][c]:
        #             path.append('!')
        #             ti += 1
        #             added = True
                    
        #         if ti == len_r:
        #             self.res = ''.join(path)
        #             return
                    
        #         if added:
        #             visited = set([(r, c)])
                
        #         for dr, dc, d in ((0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U')):
        #             path.append(d)
        #             dfs(r + dr, c + dc, visited, path, ti)
        #             path.pop()
        
        # dfs(0, 0, set([]), [], 0)
        # return self.res


sol = Solution()
# t = 'leet'
t = 'code'
print(sol.alphabetBoardPath(t))
