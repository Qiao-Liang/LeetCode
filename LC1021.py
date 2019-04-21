class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        left = right = 0
        
        for idx, c in enumerate(S):
            if c == '(':
                left += 1
            elif c == ')':
                right += 1

            if left == right:
                res.append(S[idx - left - right + 2: idx])
                left = right = 0
        
        return ''.join(res)


sol = Solution()
# s = "(()())(())"
s = "(()())(())(()(()))"
print(sol.removeOuterParentheses(s))
