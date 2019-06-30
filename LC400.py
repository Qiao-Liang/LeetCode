class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = 1
        step = 9
        base = 90
        
        while n > step:
            n -= step
            digits += 1
            step = digits * base
            base *= 10
            
        return int(str(10 ** (digits - 1) + (n - 1) / digits)[(n - 1) % digits])

        # if n < 10:
        #     return n

        # digits = 1
        # base = counts = 9

        # while True:
        #     digits += 1
        #     counts *= 10
        #     next_base = base + counts * digits
            
        #     if base < n < next_base:
        #         break
        #     else:
        #         base = next_base

        # return int(str(pow(10, digits - 1) + (n - base - 1) / digits)[(n - base - 1) % digits])


sol = Solution()
print(sol.findNthDigit(100))
