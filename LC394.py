class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        stack = [(1, [])]
        count = []
        nums = "0123456789"
        
        for ch in s:
            if ch in nums:
                count.append(ch)
            elif ch == '[':
                stack.append((int(''.join(count)), []))
                count = []
            elif ch == ']':
                temp = stack.pop()
                temp_str = temp[0] * ''.join(temp[1])
                stack[-1][1].append(temp_str)
            else:
                stack[-1][1].append(ch)

        return ''.join(stack[-1][1])


sol = Solution()
# s = "3[a2[c]]"
# s = "3[a]2[bc]"
# s = "2[abc]3[cd]ef"
s = "leetcode"
# s = "ef2[abc]3[cd]"

print(sol.decodeString(s))
