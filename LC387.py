class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        base = ord('a')
        stat = [0] * 26

        for c in s:
            stat[ord(c) - base] += 1

        cand = []
        for idx in range(0, 26):
            if stat[idx] == 1:
                cand.append(chr(idx + base))
        
        for idx, c in enumerate(s):
            if c in cand:
                return idx

        return -1


sol = Solution()
s = None
print(sol.firstUniqChar(s))
