class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        buy, sell, last_buy, last_sell = -prices[0], 0, 0, 0

        for price in prices:
            last_buy = buy
            buy = max(last_buy, last_sell - price)
            last_sell = sell
            sell = max(last_sell, last_buy + price)

        return sell


sol = Solution()
prices = [1, 2, 3, 0, 2]
print sol.maxProfit(prices)
        