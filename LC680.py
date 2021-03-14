class Solution:
    def validPalindrome(self, s: str) -> bool:
        def recurse(l, r, d):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if d:
                        return False
                    else:
                        if s[l + 1] == s[r] and s[l] == s[r - 1]:
                            return recurse(l + 1, r, True) or recurse(l, r - 1, True)
                        elif s[l + 1] == s[r]:
                            l += 1
                            d = True
                        elif s[l] == s[r - 1]:
                            r -= 1
                            d = True
                        else:
                            return False
                        
            return True
        
        return recurse(0, len(s) - 1, False)


sol = Solution()
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(sol.validPalindrome(s))

