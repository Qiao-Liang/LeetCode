class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0

        while n != 0:
            if n & 1:
                res += 1
            
            n >>= 1

        return res

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = 1
        res = 0

        while temp <= n:
            temp <<= 1

        temp >>= 1

        while n > 0:
            if n >= temp:
                res += 1
                n -= temp

            temp >>= 1

        return res


sol = Solution()
print sol.hammingWeight(11)
