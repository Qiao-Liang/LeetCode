class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10

        memo = [1] * 10
        memo[5] = 0

        for _ in range(N - 1):
            temp_memo = memo[:]
            temp_memo[0] = memo[4] + memo[6]
            temp_memo[1] = temp_memo[3] = memo[6] + memo[8]
            temp_memo[2] = memo[7] + memo[9]
            temp_memo[4] = temp_memo[6] = memo[0] + memo[3] + memo[9]
            temp_memo[7] = temp_memo[9] = memo[2] + memo[6]
            temp_memo[8] = memo[1] + memo[3]
            memo = temp_memo

        return sum(memo) % 1000000007


        # res = 0
        # k_mod = 1000000007

        # if N == 1:
        #     return 10

        # def recurse(num, n, dp):
        #     if dp[num][n]:
        #         return dp[num][n]

        #     if n == 0:
        #         return 1

        #     if num == 1:
        #         dp[num][n] = recurse(6, n - 1, dp) + recurse(8, n - 1, dp)
        #     elif num == 2:
        #         dp[num][n] = recurse(7, n - 1, dp) + recurse(9, n - 1, dp)
        #     elif num == 3:
        #         dp[num][n] = recurse(4, n - 1, dp) + recurse(8, n - 1, dp)
        #     elif num == 4:
        #         dp[num][n] = recurse(0, n - 1, dp) + recurse(3, n - 1, dp) + recurse(9, n - 1, dp)
        #     elif num == 6:
        #         dp[num][n] = recurse(0, n - 1, dp) + recurse(1, n - 1, dp) + recurse(7, n - 1, dp)
        #     elif num == 7:
        #         dp[num][n] = recurse(2, n - 1, dp) + recurse(6, n - 1, dp)
        #     elif num == 8:
        #         dp[num][n] = recurse(1, n - 1, dp) + recurse(3, n - 1, dp)
        #     elif num == 9:
        #         dp[num][n] = recurse(2, n - 1, dp) + recurse(4, n - 1, dp)
        #     elif num == 0:
        #         dp[num][n] = recurse(4, n - 1, dp) + recurse(6, n - 1, dp)

        #     return dp[num][n]

        # for num in [0, 2, 8]:
        #     res += recurse(num, N - 1, {key: [0] * N for key in range(10)})

        # for num in [1, 4, 7]:
        #     res += 2 * recurse(num, N - 1, {key: [0] * N for key in range(10)})
        
        # return res % k_mod


sol = Solution()
n = 161
print(sol.knightDialer(n))
