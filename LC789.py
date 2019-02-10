class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        self.ghost_squares = {0: set([(r, c) for r, c in ghosts])}
        self.bound = target[1] + 1
        self.can_escape = False
        self.visited = set([(0, 0)])

        def update_ghosts_squares(step):
            if step not in self.ghost_squares:
                temp = set([])

                for r, c in self.ghost_squares[step - 1]:
                    if r - 1 > -1:
                        temp.add((r - 1, c))

                    if r + 1 < self.bound:
                        temp.add((r + 1, c))

                    if c - 1 > -1:
                        temp.add((r, c - 1))
                    
                    if c + 1 < self.bound:
                        temp.add((r, c + 1))

                self.ghost_squares[step] = temp

            return self.ghost_squares[step]

        def dfs(r, c, step):
            if [r, c] == target and (r, c) not in self.ghost_squares[step - 1]:
                self.can_escape = True
                return

            update_ghosts_squares(step)

            if r - 1 > -1 and (r - 1, c) not in self.visited and (r - 1, c) not in self.ghost_squares[step]:
                self.visited.add((r - 1, c))
                dfs(r - 1, c, step + 1)

            if r + 1 < self.bound and (r + 1, c) not in self.visited and (r + 1, c) not in self.ghost_squares[step]:
                self.visited.add((r + 1, c))
                dfs(r + 1, c, step + 1)

            if c - 1 > -1 and (r, c - 1) not in self.visited and (r, c - 1) not in self.ghost_squares[step]:
                self.visited.add((r, c - 1))
                dfs(r, c - 1, step + 1)

            if c + 1 < self.bound and (r, c + 1) not in self.visited and (r, c + 1) not in self.ghost_squares[step]:
                self.visited.add((r, c + 1))
                dfs(r, c + 1, step + 1)

        dfs(0, 0, 1)
        return self.can_escape


sol = Solution()
# ghosts = [[1, 0], [0, 3]]
# target = [0, 1]
# ghosts = [[1, 0]]
# target = [2, 0]
# ghosts = [[2, 0]]
# target = [1, 0]
ghosts = [[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]]
target = [7,7]
print(sol.escapeGhosts(ghosts, target))
