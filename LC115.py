class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s, len_t = len(s), len(t)
        dp = [0] * (len_t + 1)
        dp[0] = 1

        for si in range(1 , len_s + 1):
            for ti in range(min(si, len_t), 0, -1):
                if s[si - 1] == t[ti - 1]:
                    dp[ti] += dp[ti - 1]

        return dp[-1]

        # if s == t:
        #     return 1

        # if len_s == 0 or len_t > len_s:
        #     return 0
        
        # if len_t == 0:
        #     return 1

        # dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]

        # for si in range(1, len_s + 1):
        #     for ti in range(1, len_t + 1):
        #         if s[si - 1] == t[ti - 1]:
        #             dp[si][ti] = dp[si - 1][ti - 1] + 1
        #         # else:
        #         #     dp[si][ti] = max(dp[si][ti - 1], dp[si - 1][ti])

        # return dp[-1][-1]
        
        # if dp[-1][-1] == 0:
        #     return 0

        # queue = {(len_s, len_t)}
        # max_wid = 0

        # while queue:
        #     temp_queue = set([])

        #     for r, c in queue:
        #         temp = dp[r][c]

        #         if r - 1 > -1 and c - 1 > -1 and dp[r - 1][c - 1] + 1 == temp:
        #             temp_queue.add((r - 1, c - 1))
                
        #         if r - 1 > -1 and dp[r - 1][c] == temp:
        #             temp_queue.add((r - 1, c))

        #         if c - 1 > -1 and dp[r][c - 1] == temp:
        #             temp_queue.add((r, c - 1))
            
        #     max_wid = max(max_wid, len(temp_queue))
        #     queue = temp_queue
        
        # return max_wid + 1


sol = Solution()
# s = "rabbbit"
# t = "rabbit"
s = "babgbag"
t = "bag"
# s = "b"
# t = "b"
# s = "aabb"
# t = "ab"
print(sol.numDistinct(s, t))

# [
#     [0, 0, 0, 0, 0, 0, 0], 
#     [0, 1, 1, 1, 1, 1, 1], 
#     [0, 1, 2, 2, 2, 2, 2], 
#     [0, 1, 2, 3, 3, 3, 3], 
#     [0, 1, 2, 3, 4, 4, 4], 
#     [0, 1, 2, 3, 4, 4, 4], 
#     [0, 1, 2, 3, 4, 5, 5], 
#     [0, 1, 2, 3, 4, 5, 6]
# ]

# [
#     [0, 0, 0, 0], 
#     [0, 1, 1, 1], 
#     [0, 1, 2, 2], 
#     [0, 1, 2, 2], 
#     [0, 1, 2, 3], 
#     [0, 1, 2, 3], 
#     [0, 1, 2, 3], 
#     [0, 1, 2, 3]
# ]
