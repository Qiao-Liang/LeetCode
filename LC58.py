class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        length = 0
        srt_pnt = 0

        for idx in range(len(s) - 1, -1, -1):
            if s[idx] != ' ':
                srt_pnt = idx
                break

        for idx in range(srt_pnt, -1 , -1):
            if s[idx] != ' ':
                length += 1
            else:
                break

        return length


sol = Solution()
print(sol.lengthOfLastWord("a "))
