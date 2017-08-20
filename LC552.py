class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        # When there is no A
        result = 2 ** n
        if n > 2:
            result -= 2 ** (n - 3)

        # When there is one A
        result += n * 2 ** (n - 1)
        if n > 3:
            result -= 2 ** (n - 4)
        
        if result > 10 ** 9:
            result = result % 10 ** 9 + 7

        return result

sol = Solution()
print(sol.checkRecord(3))