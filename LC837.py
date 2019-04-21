class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0: return 1
        dp = [1.0] + [0] * N
        tSum = 1.0
        
        for i in range(1, N + 1):
            dp[i] = tSum / W
            if i < K:
                tSum += dp[i]
            if 0 <= i - W < K:
                tSum -= dp[i - W]
        return sum(dp[K:])

        # self.total = 0
        # self.valid = 0
        
        # def dfs(curr_sum):
        #     if curr_sum >= K:
        #         self.total += 1
                
        #         if curr_sum <= N:
        #             self.valid += 1
        #     else:
        #         for next_num in range(1, W + 1):
        #             dfs(curr_sum + next_num)

        # dfs(0)
        # return float(self.valid) / self.total


sol = Solution()
# params = [10, 1, 10]
params = [21, 17, 10]
# params = [6, 1, 10]
print(sol.new21Game(*params))
