class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        row_bound = len(M)
        col_bound = len(M[0])
        count = 0

        # def dfs(row, col):
        #     if 0 <= row < row_bound and 0 <= col < col_bound:
        #         if M[row][col] == 1:
        #             M[row][col] = 0
                    
        #             dfs(row + 1, col)
        #             dfs(row - 1, col)
        #             dfs(row, col + 1)
        #             dfs(row, col - 1)
        
        def bfs(row, col):
            queue = [(row, col)]

            while queue:
                count = len(queue)
                while count > 0:
                    curr = queue.pop(0)
                    r, c = curr[0], curr[1]
                    if 0 <= r < row_bound and 0 <= c < col_bound and M[r][c] == 1:
                        M[r][c] = 0
                        queue.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
                
                    count -= 1
        
        for r, row in enumerate(M):
            for c, col in enumerate(row):
                if col == 1:
                    count += 1
                    # dfs(r, c)
                    bfs(r, c)
        
        return count

    # def findCircleNum(self, A):
    #     N = len(A)
    #     seen = set()
    #     def dfs(node):
    #         for nei, adj in enumerate(A[node]):
    #             if adj and nei not in seen:
    #                 seen.add(nei)
    #                 dfs(nei)
        
    #     ans = 0
    #     for i in xrange(N):
    #         if i not in seen:
    #             dfs(i)
    #             ans += 1
    #     return ans

sol = Solution()
M = [[1,1,0], [1,1,0], [0,0,1]]
M2 = [[1,1,0], [1,1,1], [0,1,1]]
M3 = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
count = sol.findCircleNum(M3)
