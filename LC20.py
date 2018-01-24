class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic_map = {')': '(', '}': '{', ']': '['}
        left_parts = dic_map.values()
        right_parts = dic_map.keys()
        stack = []

        for c in s:
            if c in left_parts:
                stack.append(c)
            elif c in right_parts:
                if stack and stack[-1] == dic_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0


sol = Solution()
print(sol.isValid("]"))
