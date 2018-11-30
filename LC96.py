class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0] * (n + 1)
        memo[0] = 1
        memo[1] = 1

        def recurse(memo, curr):
            if not memo[curr]:
                for temp in xrange(curr):
                    memo[curr] += recurse(memo, temp) * recurse(memo, curr - temp - 1)
            
            return memo[curr]

        return recurse(memo, n)


sol = Solution()
print sol.numTrees(5)
        