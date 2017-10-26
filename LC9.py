class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        else:
            rx = 0
            while x > rx:
                rx = rx * 10 + x % 10
                x = x / 10

            return x == rx or x == rx / 10

sol = Solution()
num = 12320
print(sol.isPalindrome(num))