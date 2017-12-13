class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a, len_b = len(a), len(b)
        carry = 0
        result = ''

        if len_a > len_b:
            b = '0' * (len_a - len_b) + b
        elif len_a < len_b:
            a = '0' * (len_b - len_a) + a

        for idx in range(max(len_a, len_b) - 1, -1, -1):
            temp = sorted([int(a[idx]), int(b[idx]), carry])
            result = str(reduce(lambda x, y: x ^ y, temp)) + result

            carry = temp[1]

        if carry == 1:
            result = '1' + result

        return result

sol = Solution()
print(sol.addBinary('1', '111'))
