class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = n / 5
        expo = 1

        while True:
            temp = pow(5, expo + 1)
            if n < temp:
                break
            else:
                result += n / temp
                expo += 1

        return result


sol = Solution()
print(sol.trailingZeroes(625))
