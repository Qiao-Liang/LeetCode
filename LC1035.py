class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        len_a = len(A)
        len_b = len(B)
        memo = [[None] * (len_b + 1) for _ in range(len_a + 1)]

        for idx_a in range(len_a + 1):
            for idx_b in range(len_b + 1):
                if idx_a == 0 or idx_b == 0:
                    memo[idx_a][idx_b] = 0
                elif A[idx_a - 1] == B[idx_b - 1]:
                    memo[idx_a][idx_b] = memo[idx_a - 1][idx_b - 1] + 1
                else:
                    memo[idx_a][idx_b] = max(memo[idx_a - 1][idx_b], memo[idx_a][idx_b - 1])
        
        return memo[-1][-1]


sol = Solution()
A = [1,4,2]
B = [1,2,4]
print(sol.maxUncrossedLines(A, B))
