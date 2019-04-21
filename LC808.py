class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        self.dic = {}

        def dfs(n_a, n_b, key):
            if n_a <= 0:
                if n_b > 0:
                    return 1
                else:
                    return 0.5
            elif n_b <= 0:
                return 0

            if key not in self.dic:
                temp = 0
                temp += dfs(n_a - 100, n_b, key + '1')
                temp += dfs(n_a - 75, n_b - 25, key + '2')
                temp += dfs(n_a - 50, n_b - 50, key + '3')
                temp += dfs(n_a - 25, n_b - 75, key + '4')
                self.dic[key] = 0.25 * temp

            return self.dic[key]

        return dfs(N, N, '')


sol = Solution()
N = 50
print(sol.soupServings(N))
