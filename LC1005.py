class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        idx = 0
        len_a = len(A)

        while A[idx] < 0 and idx < len_a and K > 0:
            A[idx] = -A[idx]
            idx += 1
            K -= 1
        
        A.sort()

        if K & 1:
            A[0] = -A[0]

        return sum(A)


sol = Solution()
# A = [4,2,3]
# K = 1
# A = [3,-1,0,2]
# K = 3
# A = [2,-3,-1,5,-4]
# K = 2
A = [-8,3,-5,-3,-5,-2]
K = 6
print(sol.largestSumAfterKNegations(A, K))
