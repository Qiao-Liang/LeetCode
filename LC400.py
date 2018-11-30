class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        digits = 1
        base = counts = 9

        while True:
            digits += 1
            counts *= 10
            next_base = base + counts * digits
            
            if base < n < next_base:
                break
            else:
                base = next_base

        return int(str(pow(10, digits - 1) + (n - base - 1) / digits)[(n - base - 1) % digits])


sol = Solution()
print sol.findNthDigit(1000)
