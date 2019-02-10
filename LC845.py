class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        idx = 0
        len_a = len(A)
        inc = [0] * len_a
        dec = [0] * len_a

        while idx < len_a:
            count = 0
            idx += 1

            while idx < len_a and A[idx - 1] < A[idx]:
                idx += 1
                count += 1

            inc[idx - 1] = count

        idx = len_a - 1

        while idx > 0:
            count = 0
            idx -= 1

            while idx > -1 and A[idx + 1] < A[idx]:
                idx -= 1
                count += 1

            dec[idx + 1] = count

        for idx in range(len_a):
            if inc[idx] and dec[idx]:
                res = max(res, inc[idx] + dec[idx] + 1)

        return res


sol = Solution()
# a = [2,1,4,7,3,2,5]
a = [2,2,2]
print(sol.longestMountain(a))
