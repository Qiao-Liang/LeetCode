from collections import defaultdict

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        dic = defaultdict(list)
        last = text[0]
        last_i = 0
        res = 0

        for i, c in enumerate(text[1:], start=1):
            if c != last:
                dic[last].append((last_i, i))
                last = c
                last_i = i

        dic[last].append((last_i, len(text)))
        
        for k, v in dic.items():
            ls, le = v[0]
            res = max(res, le - ls + (1 if len(v) > 1 else 0))

            for cs, ce in v[1:]:
                if cs - le == 1:
                    if len(v) == 2:
                        res = max(res, ce - ls - 1)
                    else:
                        res = max(res, ce - ls)
                else:
                    res = max(res, ce - cs + 1)

                ls, le = cs, ce
        
        return res


sol = Solution()
# text = "ababa"
# text = "aaabaaa"
# text = "aaaaa"
# text = "abcdef"
# text = "aaabbaaa"
# text = "bbababaaaa"
text = "aaaaabbbbbbaabbaabbaaabbbbab"
print(sol.maxRepOpt1(text))
