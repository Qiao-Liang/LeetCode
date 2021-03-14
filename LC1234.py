from collections import Counter#, defaultdict

class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        res = len_s = len(s)
        avg = len_s // 4
        l = 0

        for r, c in enumerate(s):
            count[c] -= 1

            while l < len_s and all(avg >= count[c] for c in 'QWER'):
                res = min(res, r - l + 1)
                count[s[l]] += 1
                l += 1

        return res
        
        # l = r = 0
        # res = len_s = len(s)
        # avg = len_s // 4
        # diff = {k: v - avg for k, v in Counter(s).items() if v - avg > 0}
        # temp = {k: 0 for k in diff}
        # len_diff = len(diff)

        # if len_diff == 0:
        #     return 0
        # if len_diff == 1 and list(diff.values())[0] == 1:
        #     return 1

        # if s[0] in temp:
        #     temp[s[0]] = 1

        # while l <= r < len_s:
        #     for k, v in temp.items():
        #         if diff[k] > v:
        #             r += 1
                    
        #             if r < len_s and s[r] in temp:
        #                 temp[s[r]] += 1
                    
        #             break
        #         elif diff[k] < v:
        #             l += 1

        #             if l < len_s and s[l] in temp:
        #                 temp[s[l]] -= 1

        #             break
        #     else:
        #         while s[l] not in temp:
        #             l += 1

        #         res = min(res, r - l + 1)
        #         l = r
        #         temp = {k: 0 for k in diff}

        #         if s[l] in temp:
        #             temp[s[l]] = 1

        # return res


sol = Solution()
# s = "QWER"
# s = "QQWE"
# s = 'QQQW'
# s = 'QQQQ'
# s = "WQWRQQQW"
s = "WWEQERQWQWWRWWERQWEQ"
print(sol.balancedString(s))
