class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1 if word1 else 1
        len2 = len(word2) + 1 if word2 else 1

        memo = [[0] * len1 for n in xrange(len2)]

        for idx1 in xrange(0, len1):
            memo[0][idx1] = idx1

        for idx2 in xrange(0, len2):
            memo[idx2][0] = idx2

        for idx1 in xrange(1, len1):
            for idx2 in xrange(1, len2):
                if word1[idx1 - 1] == word2[idx2 - 1]:
                    memo[idx2][idx1] = memo[idx2 - 1][idx1 - 1]
                else:
                    memo[idx2][idx1] = min(memo[idx2 - 1][idx1], memo[idx2][idx1 - 1], memo[idx2 - 1][idx1 - 1]) + 1

        return memo[-1][-1]


sol = Solution()
print sol.minDistance("", "abac")
