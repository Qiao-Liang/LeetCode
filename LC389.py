class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_stat = [0] * 26
        t_stat = [0] * 26
        base = ord('a')

        for c in s:
            s_stat[ord(c) - base] += 1
        
        for c in t:
            t_stat[ord(c) - base] += 1

        for idx in xrange(26):
            if s_stat[idx] != t_stat[idx]:
                return chr(idx + base)


sol = Solution()
print sol.findTheDifference("abcd", "abcde")
