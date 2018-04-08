class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        if L > R:
            return 0

        res = 0

        def is_prime(num):
            if num < 2:
                return 0
            
            factor = 2
            while factor << 1 <= num:
                if num % factor == 0:
                    return 0

                factor += 1

            return 1

        for num in xrange(L, R + 1):
            temp = 0
            while num > 0:
                temp += num & 1
                num >>= 1

            res += is_prime(temp)

        return res


sol = Solution()
print sol.countPrimeSetBits(10, 15)
