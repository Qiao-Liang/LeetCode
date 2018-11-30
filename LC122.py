class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        in_stock = False
        len_prices = len(prices)
        profit = 0

        for idx in xrange(len_prices):
            if in_stock:
                if prices[idx] >= prices[idx - 1] and (idx == len_prices - 1 or (idx < len_prices - 1 and prices[idx] > prices[idx + 1])):
                   profit += prices[idx]
                   in_stock = False
            else:
                if idx < len_prices - 1 and prices[idx] <= prices[idx + 1] and (idx == 0 or (idx > 0 and prices[idx] < prices[idx - 1])):
                   profit -= prices[idx]
                   in_stock = True
   
        return profit


sol = Solution()
prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [2, 2, 5]
print sol.maxProfit(prices)
