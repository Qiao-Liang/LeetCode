class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for n in range(len1 + 1)]

        for idx1 in range(len1):
            for idx2 in range(len2):
                dp[idx1 + 1][idx2 + 1] = max(dp[idx1 + 1][idx2], dp[idx1][idx2 + 1], dp[idx1][idx2] + (word1[idx1] == word2[idx2]))

        return len1 + len2 - 2 * dp[len1][len2]
