class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for ast in asteroids:
            if stack and stack[-1] > 0 and ast < 0:
                abs_ast = abs(ast)
                
                while stack and stack[-1] > 0 and stack[-1] < abs_ast:
                    stack.pop()
                    
                if stack:
                    if stack[-1] == abs_ast:
                        stack.pop()
                    elif stack[-1] < 0:
                        stack.append(ast)
                else:
                    stack.append(ast)
            else:
                stack.append(ast)
                
        return stack


sol = Solution()
asts = [-2, -2, 1, -2]
# asts = [5,10,-5]
print(sol.asteroidCollision(asts))
