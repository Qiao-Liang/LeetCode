from math import log

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        power = int(log(num, 2)) + 1

        while power > 2:
            base = int(num ** (1.0 / (power - 1)))
            
            if num * (base - 1) == base ** power - 1:
                return str(base)
            
            power -= 1

        return str(num - 1)

        # num = int(n)
        # power = int(log(num, 2)) + 1

        # while power > 2:
        #     base = int(num ** (1.0/(power - 1)))
            
        #     if num * (base - 1) == base ** power - 1:
        #         return str(base)
            
        #     power -= 1

        # return str(num - 1)

        # res = 1

        # while True:
        #     temp = n - 1
        #     res += 1

        #     while temp:
        #         if temp % res == 0:
        #             temp /= res
        #             temp -= 1
        #         else:
        #             break

        #     if not temp:
        #         return res


sol = Solution()
n = "15"
print(sol.smallestGoodBase(n))
        