class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        stack = [N]
        N -= 1
        opr_idx = 0

        while N > 0:
            temp = opr_idx % 4

            if temp == 0:
                stack[-1] *= N
            elif temp == 1:
                stack[-1] //= N
            elif temp == 2:
                stack.append("+")
                stack.append(N)
            elif temp == 3:
                stack.append("-")
                stack.append(N)

            N -= 1
            opr_idx += 1

        stack.reverse()

        while len(stack) > 1:
            num1 = stack.pop()
            opr = stack.pop()
            num2 = stack.pop()

            if opr == "+":
                stack.append(num1 + num2)
            elif opr == "-":
                stack.append(num1 - num2)

        return stack[0]


sol = Solution()
print(sol.clumsy(10))
