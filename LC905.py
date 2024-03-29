class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(A) - 1

        while left < right:
            if A[left] & 1 and not A[right] & 1:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            
            if not A[left] & 1:
                left += 1
            
            if A[right] & 1:
                right -= 1

        return A


sol = Solution()
a = [3,1,2,4]
print sol.sortArrayByParity(a)
        