from collections import defaultdict

class Solution:
    def countLetters(self, S: str) -> int:
        curr = S[0]
        l = r = 0
        len_s = len(S)
        res = 0
        d = 0
        
        while r < len_s:
            if S[r] == curr:
                r += 1
            else:
                d = r - l
                res += (d + 1) * d // 2
                l = r
                curr = S[l]
        
        d = r - l
        return res + (d + 1) * d // 2


sol = Solution()
# s = 'aaaba'
s = 'aaaaaaaaaa'
print(sol.countLetters(s))
