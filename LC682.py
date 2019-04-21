class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        
        for op in ops:
            if op == "D":
                stack.append(stack[-1] << 1)
            elif op == "C":
                if stack:
                    stack.pop()
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
                
        return sum(stack)


sol = Solution()
# ops = ["5","2","C","D","+"]
ops  = ["5","-2","4","C","D","9","+","+"]
print(sol.calPoints(ops))
