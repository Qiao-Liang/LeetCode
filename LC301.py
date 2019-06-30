class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        len_s = len(s)
        self.cands = set([])
        self.visited = set([])
        
        def is_valid(s):
            stack = []
            
            for c in s:
                if stack:
                    if c == ')':
                        while stack and stack[-1] != '(':
                            stack.pop()

                        if stack:
                            stack.pop()
                        else:
                            return False
                    else:
                        stack.append(c)
                else:
                    if c == ')':
                        return False
                    else:
                        stack.append(c)
        
            return "(" not in stack and ")" not in stack
        
        def recurse(idx, ts):
            if idx < len_s and (idx, ts) not in self.visited:
                self.visited.add((idx, ts))
                temp = ts + s[idx]

                if temp not in self.cands and is_valid(temp):
                        self.cands.add(temp)

                recurse(idx + 1, temp)

                if s[idx] in "()":
                    recurse(idx + 1, ts)
        
        recurse(0, '')

        if len(self.cands) > 0:
            self.cands = list(self.cands)
            self.cands.sort(key=lambda n:len(n), reverse=True)
            max_len = len(self.cands[0])
            res = [self.cands[0]]
            
            for cand in self.cands[1:]:
                if len(cand) == max_len:
                    res.append(cand)
                else:
                    break
                    
            return res
        else:
            return [""]

#     def removeInvalidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         stack = []
#         errors = []

#         for idx, ch in enumerate(s):
#             if ch == '(':
#                 stack.append((ch, idx))
#             elif ch == ')':
#                 if stack:
#                     if stack[-1][0] == '(':
#                         stack.pop()
#                     else:
#                         stack.append((ch, idx))
#                 else:
#                     errors.append((ch, idx))

#         if stack:
#             errors.extend(stack)
        
#         print(stack)
#         print(errors)


sol = Solution()
# s = "()())()"
# s = "(a)())()"
# s = ")("
# s = "n"
s = "h)))uq))v)))))))()"
# s = ")()))())))"
print(sol.removeInvalidParentheses(s))
