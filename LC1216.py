class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.memo = {}
        ls = len(s)
        s1, s2 = s, s[::-1]

        def recurse(l1, l2):
            if (l1, l2) in self.memo:
                return self.memo[(l1, l2)]

            if not l1:
                return l2
            elif not l2:
                return l1
            
            res = recurse(l1 - 1, l2 - 1) if s1[l1 - 1] == s2[l2 - 1] else 1 + min(recurse(l1 - 1, l2), recurse(l1, l2 - 1))
            self.memo[(l1, l2)] = res
            return res

        return recurse(ls, ls) <= k << 1

        # def recurse(s1, s2, m, n):
        #     if (s1, s2, m, n) in self.memo:
        #         return self.memo[(s1, s2, m, n)]

        #     if not m:
        #         return n
        #     elif not n:
        #         return m
            
        #     res = recurse(s1, s2, m - 1, n - 1) if s1[m - 1] == s2[n - 1] else 1 + min(recurse(s1, s2, m - 1, n), recurse(s1, s2, m, n - 1))
        #     self.memo[(s1, s2, m, n)] = res
        #     return res

        # ls = len(s)
        # return recurse(s, s[::-1], ls, ls) <= k * 2


sol = Solution()
p = ["abcdeca", 2]
print(sol.isValidPalindrome(*p))
