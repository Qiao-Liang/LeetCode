class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[-1][-1] = True
        
        for si in range(len_s, -1, -1):
            for pi in range(len_p - 1, -1, -1):
                first_match = si < len_s and p[pi] in {s[si], '.'}
                
                if pi + 1 < len_p and p[pi + 1] == '*':
                    dp[si][pi] = dp[si][pi + 2] or first_match and dp[si + 1][pi]
                else:
                    dp[si][pi] = first_match and dp[si + 1][pi + 1]
                    
        return dp[0][0]

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)
        memo = {}

        def dfs(idx_s, idx_p):
            if idx_s == len_s:
                for idx in range(idx_p + 1, len_p, 2):
                    if p[idx] != "*":
                        return False

                return (len_p - idx_p) & 1 == 0

            if idx_p == len_p:
                return False

            if (idx_s, idx_p) in memo:
                return memo[(idx_s, idx_p)]

            if len_p - idx_p > 1 and p[idx_p + 1] == '*':
                memo[(idx_s, idx_p)] = dfs(idx_s, idx_p + 2) or ((p[idx_p] == s[idx_s] or p[idx_p] == '.') and dfs(idx_s + 1, idx_p))
            else:
                memo[(idx_s, idx_p)] = idx_p < len_p and (p[idx_p] == s[idx_s] or p[idx_p] == '.') and dfs(idx_s + 1, idx_p + 1)
            
            return memo[(idx_s, idx_p)]

        return dfs(0, 0)


        # if not s:
        #     for ch in p[1::2]:
        #         if ch != "*":
        #             return False

        #     return not len(p) & 1

        # if len(p) > 1 and p[1] == "*":
        #     return self.isMatch(s, p[2:]) or ((p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p))
        # else:
        #     return len(p) > 0 and (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])


sol = Solution()
# s = "aa"
# p = "a"
s = "aa"
p = "a*"
# s = "ab"
# p = ".*"
# s = "aab"
# p = "c*a*b"
# s = "mississippi"
# p = "mis*is*p*."
print(sol.isMatch(s, p))
