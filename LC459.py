class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)
        
        for i in range(1, len_s):
            t = dt = s[:i]
            l = i
            
            while l < len_s and t == s[:l]:
                t += dt
                l += i
                
            if t == s:
                return True
        
        return False


sol = Solution()
# s = 'abac'
s = "ababab"
print(sol.repeatedSubstringPattern(s))
