class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647

        result = 0
        negative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            temp_divisor, temp_result = divisor, 1

            while dividend >= temp_divisor:
                dividend -= temp_divisor
                result += temp_result

                temp_divisor <<= 1
                temp_result <<= 1

        if negative:
            result = -result

        return min(max(result, -2147483648), 2147483647)

sol = Solution()
print(sol.divide(-2147483648, 0))
