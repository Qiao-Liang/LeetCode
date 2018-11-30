class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = float(numerator) / denominator
        temp = str(res).split('.')
        integer = temp[0]
        decimals = temp[1]
        len_decimals = len(decimals)

        for idx in xrange(len_decimals):
            length = 1

            while idx + length < len_decimals:
                if decimals[idx: idx + length] == decimals[idx + length: idx + 2 * length] != "0":
                    return '.'.join([integer, "{}({})".format(decimals[:idx], decimals[idx: idx + length])])

                length += 1

        return str(int(res)) if res.is_integer() else str(res)


sol = Solution()
numerator = 1
denominator = 17

print sol.fractionToDecimal(numerator, denominator)
