class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        cont = True
        
        while cont:
            cont = False
            stack = []
            temp = 1
            
            for c in s:
                if stack and stack[-1] == c:
                    temp += 1
                    
                    if temp == k:
                        cont = True
                        temp = 1
                        stack = stack[:-(k - 1)]
                    else:
                        stack.append(c)
                else:
                    temp = 1
                    stack.append(c)
            
            s = stack
            
        return ''.join(s)


sol = Solution()
# p = ["deeedbbcccbdaa", 3]
p = ["pbbcggttciiippooaais", 2]
print(sol.removeDuplicates(*p))
