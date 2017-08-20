class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [[1] * length for ch in s]

        for right in range(1, length):
            for left in range(0, right)[::-1]:
                if s[right] == s[left]:
                    dp[left][right] = dp[left + 1][right - 1] + 2 if left < right - 1 else 2
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

        return dp[0][length - 1]
        # if s == s[::-1]:
        #     return len(s)

        # n = len(s)
        # dp = [0 for j in xrange(n)]
        # dp[n-1] = 1

        # for i in xrange(n-1, -1, -1):   # can actually start with n-2...
        #     newdp = dp[:]
        #     newdp[i] = 1
        #     for j in xrange(i+1, n):
        #         if s[i] == s[j]:
        #             newdp[j] = 2 + dp[j-1]
        #         else:
        #             newdp[j] = max(dp[j], newdp[j-1])
        #     dp = newdp
                    
        # return dp[n-1]

from time import time

sol = Solution()
s = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
# s = "aabaa"
# s = "bbbab"
t = time()
print(sol.longestPalindromeSubseq(s))
print(time() - t)
