class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_A = len(A)

        if len_A < 3:
            return 0
        
        A.sort(reverse=True)
        temp = 0
        bound = len_A - 2

        while temp < bound:
            if A[temp] < A[temp + 1] + A[temp + 2]:
                return sum(A[temp: temp + 3])
            else:
                temp += 1

        return 0


sol = Solution()
a = [3,6,2,3]
print(sol.largestPerimeter(a))
        