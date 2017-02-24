class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        stack = [-1]

        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            else:
                stack.pop()
                
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    length = idx - stack[-1]

                    if length > result:
                        result = length
        
        return result