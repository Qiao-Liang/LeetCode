class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        l = 0

        for r in range(len(s)):
            maxCost -= diff[r]

            if maxCost < 0:
                maxCost += diff[l]
                l += 1
            
        return r - l + 1

        # l = r = 0
        # bound = len(s)
        # res = 0
        # temp = 0
        
        # while l <= r < bound:
        #     temp += abs(ord(s[r]) - ord(t[r]))
            
        #     if temp <= maxCost:
        #         r += 1
        #         res = max(res, r - l)
        #     else:
        #         temp -= abs(ord(s[l]) - ord(t[l]))
        #         l += 1
        #         r += 1
                
        # return res


sol = Solution()
# p = ["abcd","bcdf",3]
# p = ["abcd", "cdef", 3]
p = ["abcd", "acde", 0]
print(sol.equalSubstring(*p))
