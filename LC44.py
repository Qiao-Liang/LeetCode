class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[0][0] = True
        
        for i in range(1, len_p + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for si in range(1, len_s + 1):
            for pi in range(1, len_p + 1):
                if p[pi - 1] == '*':
                    dp[si][pi] = dp[si - 1][pi] or dp[si][pi - 1]
                else:
                    dp[si][pi] = p[pi - 1] in {'?', s[si - 1]} and dp[si - 1][pi - 1]

        return dp[-1][-1]


        # for row in dp:
        #     row[-1] = True

        # for ci in range(len_p + 1):
        #     dp[-1][ci] = True
        
        # for si in range(len_s - 1, -1, -1):
        #     for pi in range(len_p - 1, si, -1):
        #         if p[pi] == '*':
        #             dp[si][pi] = dp[si + 1][pi]
        #         else:
        #             dp[si][pi] = p[pi] in {s[si], '?'} and dp[si + 1][pi + 1]
    
        # return dp[0][0]


sol = Solution()
# s = "aab"
# p = "c*a*b"
# s = "adceb"
# p = "*a*b"
# s = "acdcb"
# p = "a*c?b"
s = "aa"
p = "*"
print(sol.isMatch(s, p))
