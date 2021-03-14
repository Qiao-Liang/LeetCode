class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_w1, len_w2 = len(word1), len(word2)
        memo = [[0] * (len_w2 + 1) for _ in range(len_w1 + 1)]
        
        for i1 in range(1, len_w1 + 1):
            for i2 in range(1, len_w2 + 1):
                if word1[i1 - 1] == word2[i2 - 1]:
                    memo[i1][i2] = memo[i1 - 1][i2 - 1] + 1
                else:
                    memo[i1][i2] = max(memo[i1 - 1][i2], memo[i1][i2 - 1])

        return len_w1 + len_w2 - (memo[-1][-1] << 1)

        # len1, len2 = len(word1), len(word2)
        # dp = [[0] * (len2 + 1) for n in range(len1 + 1)]

        # for idx1 in range(len1):
        #     for idx2 in range(len2):
        #         dp[idx1 + 1][idx2 + 1] = max(dp[idx1 + 1][idx2], dp[idx1][idx2 + 1], dp[idx1][idx2] + (word1[idx1] == word2[idx2]))

        # return len1 + len2 - 2 * dp[len1][len2]


sol = Solution()
params = ["delete", "leet"]
print(sol.minDistance(*params))
