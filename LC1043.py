class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        len_a = len(A)
        memo = [0] * (len_a + K)

        for idx in range(len_a):
            curr_max = 0

            for k in range(1, min(K, idx + 1) + 1):
                curr_max = max(curr_max, A[idx - k + 1])
                memo[idx] = max(memo[idx], memo[idx - k] + curr_max * k)

        return memo[len_a - 1]

sol = Solution()
A = [1,15,7,9,2,5,10]
# A = [1, 15, 7, 9]
K = 3
print(sol.maxSumAfterPartitioning(A, K))
