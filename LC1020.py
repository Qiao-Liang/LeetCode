class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row_bound = len(A)
        col_bound = len(A[0])
        last_row_idx = row_bound - 1
        last_col_idx = col_bound - 1
        res = 0

        def bfs(nodes):
            dirs = [-1, 0, 1, 0, -1]

            for node in nodes:
                if A[node[0]][node[1]] == 1:
                    queue = [node]
                    A[node[0]][node[1]] = 0

                    while queue:
                        r, c = queue.pop(0)

                        for idx in range(4):
                            tr = dirs[idx]
                            tc = dirs[idx + 1]

                            if -1 < (r + tr) < row_bound and -1 < (c + tc) < col_bound and A[r + tr][c + tc] == 1:
                                A[r + tr][c + tc] = 0
                                queue.append((r + tr, c + tc))

        bfs([(0, idx) for idx in range(col_bound) if A[0][idx] == 1])
        bfs([(idx, 0) for idx in range(row_bound) if A[idx][0] == 1])
        bfs([(last_row_idx, idx) for idx in range(col_bound) if A[last_row_idx][idx] == 1])
        bfs([(idx, last_col_idx) for idx in range(row_bound) if A[idx][last_col_idx] == 1])

        for r in range(row_bound):
            for c in range(col_bound):
                res += A[r][c]

        return res


sol = Solution()
# m = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
m = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(sol.numEnclaves(m))
        