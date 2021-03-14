class Solution:
    def interpret(self, command: str) -> str:
        res = []
        stk = []
        
        for c in command:
            if c == 'G':
                res.append('G')
            elif c == ')':
                p = stk.pop()
                l = 0
                
                while p != '(':
                    p = stk.pop()
                    l += 1

                res.append('o' if l == 0 else 'al')
            else:        
                stk.append(c)
        
        return ''.join(res)
