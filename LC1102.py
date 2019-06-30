class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
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
m = [[5,4,5],[1,2,6],[7,4,6]]
print(sol.maximumMinimumPath(m))
