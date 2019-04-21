class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        memo = {}
        calc = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b}
        oprs = [idx for idx, ch in enumerate(input) if ch in "+-*"]

        def dfs(srt, end, oprs):
            if (srt, end) in memo:
                return memo[(srt, end)]

            if len(oprs) == 0:
                return [int(input[srt: end])]

            res = []

            for idx, opr in enumerate(oprs):
                left = dfs(srt, opr, oprs[:idx])
                right = dfs(opr + 1, end, oprs[idx + 1:])

                for l in left:
                    for r in right:
                        res.append(calc[input[opr]](l, r))

            memo[(srt, end)] = res
            return res

        return dfs(0, len(input), oprs)


sol = Solution()
# expr = "2-1-1"
expr = "2*3-4*5"
print(sol.diffWaysToCompute(expr))
