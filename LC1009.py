class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        temp = 1
        
        while temp < N:
            temp <<= 1

        temp -= 1

        return ~N & temp


sol = Solution()
print(sol.bitwiseComplement(5))
