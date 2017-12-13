# class Solution(object):
#     count = 0

#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         self.dfs(n)

#         return self.count
    
#     def dfs(self, n):
#         if n == 0:
#             self.count += 1
#             return
#         elif n < 0:
#             return
#         else:
#             for num in [1, 2]:
#                 self.dfs(n - num)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        s1 = 1
        s2 = 2
        cnt = 3

        while cnt <= n:
            temp = s1 + s2
            s1 = s2
            s2 = temp

            cnt += 1

        return s2

        # if n == 1:
        #     return 1

        # s1 = ['1']
        # s2 = ['11', '2']
        # cnt = 3

        # while cnt <= n:
        #     cnt += 1
        #     temp = []
            
        #     for lst in s1:
        #         left = '2' + lst
        #         right = lst + '2'

        #         if left == right:
        #             temp.append(left)
        #         else:
        #             temp.extend([left, right])

        #     for lst in s2:
        #         left = '1' + lst
        #         right = lst + '1'

        #         if left == right:
        #             temp.append(left)
        #         else:
        #             temp.extend([left, right])

        #     s1 = s2
        #     s2 = list(set(temp))

        # return len(s2)

from time import time
sol = Solution()
t = time()
print(sol.climbStairs(10))
print(time() - t)
