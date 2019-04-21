class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = 0
        right = len(S)
        res = [None] * (right + 1)
        res_idx = 0
        
        for c in S:
            if c == 'D':
                res[res_idx] = right
                right -= 1
            elif c == 'I':
                res[res_idx] = left
                left += 1
            
            res_idx += 1
        
        res[res_idx] = left
        return res


sol = Solution()
s = "IDID"
# s = "III"
# s = "DDI"
print(sol.diStringMatch(s))
