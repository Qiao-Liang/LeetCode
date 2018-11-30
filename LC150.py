class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        opers = "+-*/"
        stack = []

        for token in tokens:
            if token in opers:
                r_op = stack.pop()
                l_op = stack.pop()

                if token == '+':
                    stack.append(l_op + r_op)
                elif token == '-':
                    stack.append(l_op - r_op)
                elif token == '*':
                    stack.append(l_op * r_op)
                elif token == '/':
                    stack.append(int(float(l_op) / r_op))
            else:
                stack.append(int(token))

        return stack[-1]


sol = Solution()
# tokens = ["2", "1", "+", "3", "*"]
# tokens = ["4", "13", "5", "/", "+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print sol.evalRPN(tokens)
        