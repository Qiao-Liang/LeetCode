class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idx_a, idx_b = len(a) - 1, len(b) - 1
        res = []
        carry = 0

        while idx_a > -1 and idx_b > -1:
            temp_a, temp_b = int(a[idx_a]), int(b[idx_b])
            res.append(temp_a ^ temp_b ^ carry)
            carry = temp_a and temp_b or temp_a and carry or temp_b and carry

            idx_a -= 1
            idx_b -= 1

        while idx_a > -1:
            temp_a = int(a[idx_a])
            res.append(temp_a ^ carry)
            carry = temp_a and carry

            idx_a -= 1

        while idx_b > -1:
            temp_b = int(b[idx_b])
            res.append(temp_b ^ carry)
            carry = temp_b and carry

            idx_b -= 1

        if carry:
            res.append(1)

        return ''.join(map(str, reversed(res)))


        # len_a, len_b = len(a), len(b)
        # carry = 0
        # result = ''

        # if len_a > len_b:
        #     b = '0' * (len_a - len_b) + b
        # elif len_a < len_b:
        #     a = '0' * (len_b - len_a) + a

        # for idx in range(max(len_a, len_b) - 1, -1, -1):
        #     temp = sorted([int(a[idx]), int(b[idx]), carry])
        #     result = str(reduce(lambda x, y: x ^ y, temp)) + result

        #     carry = temp[1]

        # if carry == 1:
        #     result = '1' + result

        # return result

sol = Solution()
print(sol.addBinary('1', '111'))
