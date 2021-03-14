from collections import defaultdict

class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        phs_set = defaultdict(list)
        phs_list = [ph.split(' ') for ph in phrases]
        res = set([])
        
        for i, ph in enumerate(phs_list):
            phs_set[ph[0]].append((i, ph))
            
        for i, ph in enumerate(phs_list):
            if ph[-1] in phs_set:
                for ti, temp in phs_set[ph[-1]]:
                    if ti != i:
                        res.add(' '.join(ph + temp[1:]))
        
        res = list(res)
        res.sort()
        return res


sol = Solution()
p = ["writing code","code rocks"]
# p = ["mission statement",
#                   "a quick bite to eat",
#                   "a chip off the old block",
#                   "chocolate bar",
#                   "mission impossible",
#                   "a man on a mission",
#                   "block party",
#                   "eat my words",
#                   "bar of soap"]
# p = ["a","b","a"]
print(sol.beforeAndAfterPuzzles(p))
