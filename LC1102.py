from heapq import heappop, heappush

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rb, cb = len(A) - 1, len(A[0]) - 1
        heap = [(-A[0][0], 0, 0)]
        res = float('inf')
        visited = set([(0, 0)])
        dirs = [0, 1, 0, -1, 0]

        while True:
            v, r, c = heappop(heap)
            res = min(res, -v)

            if (r, c) == (rb, cb):
                return res
            
            for i in range(4):
                tr, tc = r + dirs[i], c + dirs[i + 1]

                if -1 < tr <= rb and -1 < tc <= cb and (tr, tc) not in visited:
                    heappush(heap, (-A[tr][tc], tr, tc))
                    visited.add((tr, tc))


        # self.curr_max = 0
        # self.res = A[0][0]
        # rb = len(A) - 1
        # cb = len(A[0]) - 1
        
        # def dfs(r, c, visited):
        #     if -1 < r <= rb and -1 < c <= cb and (r, c) not in visited:
        #         visited.add((r, c))
            
        #         if r == rb and c == cb:
        #             temp = [A[r][c] for r, c in visited]
        #             temp_sum = sum(temp)
        #             min_temp = min(temp)
                    
        #             if temp_sum > self.curr_max:
        #                 self.res = min_temp
        #             elif temp_sum == self.curr_max:
        #                 self.res = min(self.res, min_temp)   
        #         else:
        #             dfs(r + 1, c, visited)
        #             dfs(r - 1, c, visited)
        #             dfs(r, c + 1, visited)
        #             dfs(r, c - 1, visited)
        #             visited.remove((r, c))

        # dfs(0, 0, set([]))
        # print(self.curr_max)
        
        # return self.res


sol = Solution()
# m = [[5,4,5],[1,2,6],[7,4,6]]
m = [
    [9,2,5],
    [3,5,1],
    [6,7,8]
]
# m = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
print(sol.maximumMinimumPath(m))
