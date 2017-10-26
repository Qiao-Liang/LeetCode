class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        str = str.strip()
        sign = 1
        nums = '0123456789'
        result = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if str and str[0] in '+-':
            sign = 1 - 2 * (str[0] == '-')
            str = str[1:]

        for c in str:
            if c in nums:
                result = result * 10 + int(c)
            else:
                break

        if (sign == 1 and result > INT_MAX):
            return INT_MAX
        elif (sign == -1 and result * sign < INT_MIN):
            return INT_MIN
        else:
            return result * sign

sol = Solution()
input = '   -0012a42      '
print(sol.myAtoi(input))
