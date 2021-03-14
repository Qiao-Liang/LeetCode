class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        to_remove = set([])
        res = []
        
        for i, c in enumerate(s):
            if c == '(':
                stk.append((c, i))
            elif c == ')':
                if stk and stk[-1][0] == '(':
                    stk.pop()
                else:
                    to_remove.add(i)

        to_remove.update([n[1] for n in stk])

        for i, c in enumerate(s):
            if i not in to_remove:
                res.append(c)
        
        return ''.join(res)


sol = Solution()
# s = "lee(t(c)o)de)"
# s = 'a)b(c)d'
s = '))(('
print(sol.minRemoveToMakeValid(s))
