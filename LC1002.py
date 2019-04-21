class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        stat = [[0] * 26 for _ in range(len(A))]
        base = ord('a')
        res = []

        for idx, word in enumerate(A):
            for ch in word:
                stat[idx][ord(ch) - base] += 1

        for idx in range(26):
            min_temp = min([st[idx] for st in stat])
            
            if min_temp:
                res.extend([chr(idx + base)] * min_temp)

        return res


sol = Solution()
a = ["bella","label","roller"]
print(sol.commonChars(a))
