class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        set_a = set(A)
        res = 0

        for idx, left in enumerate(A):
            for right in A[idx + 1:]:
                temp = 0
                a = left
                b = right

                while True:
                    a, b = b, a + b

                    if b in set_a:
                        temp += 1
                    else:
                        break

                res = max(res, temp + 2 if temp else 0)

        return res


sol = Solution()
# a = [1,2,3,4,5,6,7,8]
# a = [1,3,7,11,12,14,18]
a = [1,3,5]
print(sol.lenLongestFibSubseq(a))
