class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n & 1

        while n > 0:
            n >>= 1
            curr = n & 1

            if curr == last:
                return False

            last = curr

        return True


sol = Solution()
print sol.hasAlternatingBits(5)
