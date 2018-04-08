class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            cache = [0] * (n + 1)
            cache[2] = 1

            for num in xrange(2, n + 1):
                temp = 0
                for loop in xrange(2, num / 2 + 1):
                    temp = max(temp, loop * (num - loop), loop * cache[num - loop])

                cache[num] = temp

        return cache[-1]


    def integerBreak2(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [0] * (n + 1)

        def dfs(n):
            if n == 2:
                return 1

            if cache[n]:
                return cache[n]
            else:
                temp = 0
                for cand in xrange(1, n / 2 + 1):
                    temp = max(temp, cand * (n - cand), cand * dfs(n - cand))

                cache[n] = temp
                return temp

        return dfs(n)


sol = Solution()
print sol.integerBreak(4)
        