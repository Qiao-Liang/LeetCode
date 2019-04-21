class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def split(expr):
            idx = 1
            bound = len(expr) - 1
            res = []

            while idx < bound:
                if expr[idx] == "(":
                    stack = ["("]
                    idx += 1
                    temp_idx = idx

                    while stack:
                        if expr[temp_idx] == "(":
                            stack.append("(")
                        elif expr[temp_idx] == ")":
                            stack.pop()
                        
                        temp_idx += 1

                    res.append(expr[idx - 1: temp_idx])
                    idx = temp_idx
                elif expr[idx] != " ":
                    temp_idx = idx

                    while temp_idx < bound and expr[temp_idx] != " ":
                        temp_idx += 1

                    res.append(expr[idx: temp_idx])
                    idx = temp_idx
                else:
                    idx += 1

            return res

        def is_number(n):
            return n.replace("-", "").isnumeric()

        def recurse(expr, args):
            temp = split(expr)
            oper = temp[0]
            local_args = args.copy()

            if oper == "let":
                len_temp = len(temp)
                idx = 1

                while idx + 1 < len_temp:
                    if is_number(temp[idx + 1]):
                        local_args[temp[idx]] = int(temp[idx + 1])
                    elif temp[idx + 1] in local_args:
                        local_args[temp[idx]] = local_args[temp[idx + 1]]
                    else:
                        local_args[temp[idx]] = recurse(temp[idx + 1], local_args)
                    
                    idx += 2

                if is_number(temp[-1]):
                    return int(temp[-1])
                elif temp[-1] in local_args:
                    return local_args[temp[-1]]
                else:
                    return recurse(temp[-1], local_args)
            else:
                func = {"add": lambda x, y: x + y, "mult": lambda x, y: x * y}
                
                if is_number(temp[1]):
                    oprand1 = int(temp[1])
                elif temp[1] in local_args:
                    oprand1 = local_args[temp[1]]
                else:
                    oprand1 = recurse(temp[1], local_args)

                if is_number(temp[2]):
                    oprand2 = int(temp[2])
                elif temp[2] in local_args:
                    oprand2 = local_args[temp[2]]
                else:
                    oprand2 = recurse(temp[2], local_args)
                
                return func[oper](oprand1, oprand2)

        return recurse(expression, {})


sol = Solution()
# expr = "(let x 2 (mult x 5))"
# expr = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
# expr = "(let x 1 y 2 x (add x y) (add x y))"
# expr = "(let x 2 (add (let x 3 (let x 4 x)) x))"
# expr = "(let a1 3 b2 (add a1 1) b2)"
expr = "(let x 7 -12)"
# expr = "(let x -2 y x y)"
print(sol.evaluate(expr))
