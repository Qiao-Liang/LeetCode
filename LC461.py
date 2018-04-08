class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor_res = x ^ y
        # temp = 1
        # digits = 0
        res = 0

        while xor_res > 0:
            res += xor_res % 2
            xor_res >>= 1

        # while temp <= xor_res:
        #     digits += 1
        #     temp <<= 1

        # while digits > 0:
        #     res += xor_res & 1
        #     xor_res >>= 1
        #     digits -= 1

        return res

        # str_long = "{0:b}".format(x)
        # str_short = "{0:b}".format(y)
        # len_long = len(str_long)
        # len_short = len(str_short)
        
        # if len_long < len_short:
        #     len_long, len_short = len_short, len_long
        #     str_long, str_short = str_short, str_long
        
        # str_short = "0" * (len_long - len_short) + str_short
        # res = 0

        # for idx in xrange(len_long):
        #     if str_long[idx] != str_short[idx]:
        #         res += 1

        # return res


sol = Solution()
print sol.hammingDistance(4, 1)
