class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a = sum(A)
        sum_b = sum(B)
        target = (sum_a + sum_b) / 2
        idx_a = len(A) - 1
        idx_b = len(B) - 1
        A.sort()
        B.sort()

        while idx_a > -1 and idx_b > -1:
            temp_a = sum_a - A[idx_a] + B[idx_b]
            temp_b = sum_b - B[idx_b] + A[idx_a]

            if temp_a < temp_b:
                idx_a -= 1
            elif temp_a > temp_b:
                idx_b -= 1
            else:
                return [A[idx_a], B[idx_b]]


sol = Solution()
# A = [1,1]
# B = [2,2]
# A = [1,2]
# B = [2,3]
# A = [2]
# B = [1,3]
A = [1,2,5]
B = [2,4]
print(sol.fairCandySwap(A, B))
        