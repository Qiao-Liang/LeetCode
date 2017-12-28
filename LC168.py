class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return None

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        temp = 26
        power = 0

        while n > temp:
            power += 1
            temp += pow(26, power + 1)

        while n > 26:
            base = pow(26, power)
            digit = 1

            while (digit + 1) * base < n:
                digit += 1

            result += alphabet[digit - 1]
            n -= digit * base
            power -= 1

        result += alphabet[n - 1]

        return result


sol = Solution()
print(sol.convertToTitle(703))
