class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        srt = ord('A') - 1
        power = len(s) - 1
        result = 0

        for c in s:
            result += (ord(c) - srt) * pow(26, power)
            power -= 1

        return result


sol = Solution()
print(sol.titleToNumber('ZZ'))
