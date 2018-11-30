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

        # cand = set([chr(idx + base) for (idx, val) in enumerate(stat) if val == 1])

        # for idx, c in enumerate(s):
        #     if c in cand:
        #         return idx

        for idx, c in enumerate(s):
            if stat[ord(c) - base] == 1:
                return idx
        
        return -1

        # if not s:
        #     return -1

        # base = ord('a')
        # stat = [0] * 26

        # for c in s:
        #     stat[ord(c) - base] += 1

        # cand = []
        # for idx in range(0, 26):
        #     if stat[idx] == 1:
        #         cand.append(chr(idx + base))
        
        # for idx, c in enumerate(s):
        #     if c in cand:
        #         return idx

        # return -1


sol = Solution()
s = None
# s = "loveleetcode"
print(sol.firstUniqChar(s))
