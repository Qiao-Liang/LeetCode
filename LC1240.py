class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.dp = [[0] * 14 for _ in range(14)]

        def recurse(m, n):
            if m == n:
                return 1

            vm = float('inf')
            hm = float('inf')

            if self.dp[m][n] != 0:
                return self.dp[m][n]

            for i in range(1, m // 2 + 1):
                hm = min(recurse(i, n) + recurse(m - i, n), hm)
            
            for i in range(1, n // 2 + 1):
                vm = min(recurse(m, i), recurse(m, n - i), vm)

            self.dp[m][n] = min(vm, hm)
            return self.dp[m][n]

        return recurse(n, m)

        # if n < m:
        #     n, m = m, n

        # res = 0

        # while m:
        #     n, m = m, n % m
        #     res += 1

        # res += n
        # return res


sol = Solution()
# p = [2, 3]
p = [5, 8]
# p = [11, 13]
print(sol.tilingRectangle(*p))
