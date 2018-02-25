class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0

        base = 1
        while base <= m:
            base <<= 1

        if n < base:
            base >>= 1

            return base + self.rangeBitwiseAnd(m - base, n - base)
        else:
            return 0


sol = Solution()
print sol.rangeBitwiseAnd(5, 7)
