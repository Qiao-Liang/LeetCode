class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def add(a, b):
            carry = 0

            while b:
                carry = (a & b) << 1
                a = a ^ b
                b = carry

            return a

        rev = False

        if a < 0 and b > 0 and abs(a) < b or a > 0 and b < 0 and abs(b) < a:
            rev = True
            a = add(~a, 1)
            b = add(~b, 1)

        res = add(a, b)

        return add(~res, 1) if rev else res


sol = Solution()
print(sol.getSum(3, 2))
