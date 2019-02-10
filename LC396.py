class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_a = sum(A)
        max_sum = 0
        end_idx = len(A) - 1

        for idx, num in enumerate(A):
            max_sum += idx * num

        last_sum = max_sum

        for idx in range(end_idx, 0, -1):
            last_sum = last_sum + sum_a - A[idx] - A[idx] * end_idx
            max_sum = max(max_sum, last_sum)

        return max_sum


sol = Solution()
A = [4, 3, 2, 6]
print(sol.maxRotateFunction(A))
        