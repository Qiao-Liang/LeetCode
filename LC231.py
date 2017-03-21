"""
Power of Two
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 2:
            if n % 2 == 0:
                return self.isPowerOfTwo(n / 2)
            else:
                return False
        elif n == 2:
            return True
        else:
            return False

    def isPowerOfTwo_Easier(self, n):
        """
        Bit manipulation
        """
        return (n > 0) and (n & (n - 1)) == 0
