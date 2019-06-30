class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_a = len(A)
        memo = [[0] * len_a for _ in range(len_a)]

        for end in range(2, len_a):
            for srt in range(end - 2, -1, -1):
                temp = A[srt] * A[end]
                memo[srt][end] = min([memo[srt][k] + memo[k][end] + temp * A[k] for k in range(srt + 1, end)] or [0])

        return memo[0][-1]


sol = Solution()
a = [3,7,4,5]
# a = [1,3,1,4,1,5]
print(sol.minScoreTriangulation(a))
