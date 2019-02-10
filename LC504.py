class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        res = []
        positive = True

        if num < 0:
            num = -num
            positive = False

        while num:
            res.append(num % 7)
            num //= 7

        res = ''.join(map(str, reversed(res)))

        return res if positive else '-' + res


sol = Solution()
num = -7
print(sol.convertToBase7(num))
        