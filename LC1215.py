class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        self.res = set([])

        def dfs(n):
            if low <= n <= high:
                self.res.add(n)
            elif n == 0 or n > high:
                return
            
            ld = n % 10
            na = n * 10 + ld - 1
            nb = na + 2

            if ld == 0:
                dfs(nb)
            elif ld == 9:
                dfs(na)
            else:
                dfs(na)
                dfs(nb)

        for i in range(10):
            dfs(i)

        res = list(self.res)
        res.sort()
        return res


sol = Solution()
p = [0, 21]
print(sol.countSteppingNumbers(*p))
