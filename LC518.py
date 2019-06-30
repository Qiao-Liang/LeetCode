class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for idx in range(coin, amount + 1):
                dp[idx] += dp[idx - coin]
        
        return dp[-1]


sol = Solution()
amount = 5
coins = [1, 2, 5]
print(sol.change(amount, coins))
