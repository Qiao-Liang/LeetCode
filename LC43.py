class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        
        base = 1
        base_ord = ord('0')
        mul_tbl = [[0] * 10 for _ in xrange(10)]
        res = 0
        
        for r in xrange(10):
            for c in xrange(10):
                mul_tbl[r][c] = r * c

        for d1 in reversed(num1):
            temp_base = 1
            n1 = ord(d1) - base_ord

            for d2 in reversed(num2):
                res += mul_tbl[n1][ord(d2) - base_ord] * temp_base * base
                temp_base *= 10

            base *= 10

        return str(res)


sol = Solution()
# num1 = '2'
# num2 = '3'
num1 = "123"
num2 = "456"
print sol.multiply(num1, num2)
