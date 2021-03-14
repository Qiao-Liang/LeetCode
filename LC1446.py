class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        i, l = 0, len(s)
        
        while i < l:
            ri = i + 1
            
            while ri < l and s[ri] == s[i]:
                ri += 1
            
            res = max(res, ri - i)
            i = ri
            
        return res


sol = Solution()
s = "leetcode"
print(sol.maxPower(s))
