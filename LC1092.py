class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def lcs(str1, str2):
            len_a, len_b = len(str1), len(str2)
            dp = [[""] * (len_b + 1) for _ in range(len_a + 1)]

            for r in range(len_a):
                for c in range(len_b):
                    if str1[r] == str2[c]:
                        dp[r + 1][c + 1] = dp[r][c] + str1[r]
                    else:
                        dp[r + 1][c + 1] = max(dp[r + 1][c], dp[r][c + 1], key=len)
            
            return dp[-1][-1]

        res = ""
        r = c = 0

        for ch in lcs(str1, str2):
            while str1[r] != ch:
                res += str1[r]
                r += 1
            
            while str2[c] != ch:
                res += str2[c]
                c += 1

            res += ch
            r += 1
            c += 1

        return res + str1[r:] + str2[c:]


sol = Solution()
str1 = "abac"
str2 = "cab"
# str1 = "aabbabaa"
# str2 = "aabbbbbbaa"
# str1 = "babbbbaa"
# str2 = "baabbbbba"
print(sol.shortestCommonSupersequence(str1, str2))
