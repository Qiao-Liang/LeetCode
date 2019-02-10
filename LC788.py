class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        must_have = '2569'
        must_not_have = '347'
        result = 0
        
        for num in range(1, N + 1):
            temp = 0

            for ch in str(num):
                if ch in must_have:
                    temp = 1
                elif ch in must_not_have:
                    temp = 0
                    break

            result += temp

        return result


sol = Solution()
print(sol.rotatedDigits(10))
