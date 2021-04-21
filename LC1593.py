class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        ls = len(s)
        l = 0
        res = 0
        
        while l < ls:
            if s[l] not in seen:
                res += 1
                seen.add(s[l])
                l += 1
            else:
                r = l + 1
                
                while r <= ls and s[l: r] in seen:
                    r += 1
                
                if s[l:r] not in seen:
                    res += 1
                    seen.add(s[l: r])
                
                l = r
                
        return res


sol = Solution()
s = "aa"
print(sol.maxUniqueSplit(s))
