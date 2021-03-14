class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c == ')':
                temp = []
                
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                    
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(c)
                
        return ''.join(stack)


sol = Solution()
# s = "(abcd)"
# s = "(u(love)i)"
# s = "(ed(et(oc))el)"
# s = "a(bcdefghijkl(mno)p)q"
s = ""
print(sol.reverseParentheses(s))
