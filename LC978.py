class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        idx = 0
        len_a = len(A)
        res = 1
        count = 1

        while idx + 1 < len_a:
            if (idx & 1 and A[idx] > A[idx + 1]) or ((not idx & 1) and A[idx] < A[idx + 1]):
                count += 1
            else:
                res = max(res, count)
                count = 1

            idx += 1

        res = max(res, count)
        count = 1
        idx = 0

        while idx + 1 < len_a:
            if (idx & 1 and A[idx] < A[idx + 1]) or ((not idx & 1) and A[idx] > A[idx + 1]):
                count += 1
            else:
                res = max(res, count)
                count = 1

            idx += 1
        
        res = max(res, count)

        return res


sol = Solution()
# a = [9,4,2,10,7,8,8,1,9]
# a = [4,8,12,16, 1]
# a = [100]
# a = [0,1,1,0,1,0,1,1,0,0]
# a = [2,0,2,4,2,5,0,1,2,3]
a = [0,8,45,88,48,68,28,55,17,24]
print(sol.maxTurbulenceSize(a))
        