class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            temp = 9
            poss = 9
            res = 10

            while n > 1 and poss > 0:
                temp = temp * poss
                res += temp
                poss -= 1
                n -= 1

            return res


sol = Solution()
print sol.countNumbersWithUniqueDigits(12)
