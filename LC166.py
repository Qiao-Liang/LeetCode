class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        rem = numerator % denominator
        intg = numerator // denominator

        if rem == 0:
            return str(intg)

        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        res = []
        rem_pos = {}
        
        while rem and rem not in rem_pos:
            rem_pos[rem] = len(rem_pos)
            numerator = rem * 10
            res.append(str(numerator // denominator))
            rem = numerator % denominator

        if rem:
            res.insert(rem_pos[rem], '(')
            res.append(')')

        return ''.join([sign, str(intg), '.'] + res)

        # return ''.join([sign, str(intg), '.']) + (''.join(res) if rem else ''.join(res[:rem_pos[rem]] + ['('] + res[rem_pos[rem]:] + [')']))

        # res = float(numerator) / denominator
        # temp = str(res).split('.')
        # integer = temp[0]
        # decimals = temp[1]
        # len_decimals = len(decimals)

        # for idx in xrange(len_decimals):
        #     length = 1

        #     while idx + length < len_decimals:
        #         if decimals[idx: idx + length] == decimals[idx + length: idx + 2 * length] != "0":
        #             return '.'.join([integer, "{}({})".format(decimals[:idx], decimals[idx: idx + length])])

        #         length += 1

        # return str(int(res)) if res.is_integer() else str(res)


sol = Solution()
numerator = 1
denominator = 7
print(sol.fractionToDecimal(numerator, denominator))
