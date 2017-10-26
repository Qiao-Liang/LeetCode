class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        start = 0
        nums = '0123456789'

        for c in s:
            if c not in nums:
                start += 1

        result = int(s[:start] + s[start:][::-1])

        print result

        if result > 2147483647 or result < -2147483648:
            return 0
        else:
            return result

sol = Solution()
print(sol.reverse(-1463847412))
