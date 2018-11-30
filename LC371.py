class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b

        if b == 0:
            return a

        carry = 0

        # if a < 0:
        #     a = ~a

        while b:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a

        # bin_a = bin(a)[2:]
        # bin_b = bin(b)[2:]

        # idx_a = len(bin_a) - 1
        # idx_b = len(bin_b) - 1
        # carry = 0
        # res = []

        # while idx_a > -1 and idx_b > -1:
        #     ch_a = int(bin_a[idx_a])
        #     ch_b = int(bin_b[idx_b])

        #     res.append(str(ch_a ^ ch_b ^ carry))
        #     carry = ch_a and ch_b or ch_a and carry or ch_b and carry

        #     idx_a -= 1
        #     idx_b -= 1

        # while idx_a > -1:
        #     res.append(bin_a[idx_a])

        #     idx_a -= 1

        # while idx_b > -1:
        #     res.append(bin_b[idx_b])

        #     idx_b -= 1

        # if carry == 1:
        #     res.append('1')

        # return int(''.join(reversed(res)), 2)


sol = Solution()
print sol.getSum(-2, 3)
