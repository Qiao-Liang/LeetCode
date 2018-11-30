class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        if amount < min(coins):
            return -1
        
        min_count = [-1] * (amount + 1)

        for coin in coins:
            if -1 < coin <= amount:
                min_count[coin] = 1

        for temp_sum in xrange(1, amount + 1):
            for coin in coins:
                if temp_sum - coin > 0 and min_count[temp_sum - coin] != -1:
                    if min_count[temp_sum] == -1:
                        min_count[temp_sum] = min_count[temp_sum - coin] + 1
                    elif min_count[temp_sum - coin] + 1 < min_count[temp_sum]:
                        min_count[temp_sum] = min_count[temp_sum - coin] + 1
        
        return min_count[-1]


sol = Solution()
# print sol.coinChange([1, 2, 5], 11)
# print sol.coinChange([1], 0)
# print sol.coinChange([1, 2147483647], 2)
print sol.coinChange([370,417,408,156,143,434,168,83,177,280,117], 9953)
