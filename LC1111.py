class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        stk_a = []
        stk_b = []
        res = [0] * len(seq)
        last_in = []
        
        for idx, c in enumerate(seq):
            if c == '(':
                if len(stk_b) < len(stk_a):
                    stk_b.append(c)
                    res[idx] = 1
                    last_in.append(1)
                else:
                    stk_a.append(c)
                    res[idx] = 0
                    last_in.append(0)
            else:
                if last_in[-1] == 0:
                    stk_a.pop()
                    res[idx] = 0
                else:
                    stk_b.pop()
                    res[idx] = 1

                last_in.pop()
        
        return res  


sol = Solution()
# s = "(()())"
s = "()(())()"
print(sol.maxDepthAfterSplit(s))
