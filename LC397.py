class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}

        def dfs(n, rpl):
            if n in cache:
                return cache[n]

            if n == 1:
                return rpl

            if n & 1:
                temp = 1 + min(dfs(n + 1, rpl), dfs(n - 1, rpl))
            else:
                temp = 1 + dfs(n // 2, rpl)

            cache[n] = temp
            return temp

        return dfs(n, 0)

    def integerReplacement2(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0

        while n > 1:
            res += 1

            if not n & 1:
                n //= 2
            elif not n & 2 or n == 3:
                n -= 1
            else:
                n += 1

        return res


sol = Solution()
print(sol.integerReplacement(99))
