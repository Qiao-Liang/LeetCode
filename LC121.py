class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0

        buy_price, res = prices[0], 0

        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            else:
                res = max(res, price - buy_price)
        
        return res

        # if not prices:
        #     return 0

        # len_prices = len(prices)
        # max_list = [0] * len_prices
        # min_list = [0] * len_prices
        # min_list[0] = prices[0]
        # max_list[-1] = prices[-1]

        # for idx in xrange(1, len_prices):
        #     if prices[idx] < min_list[idx - 1]:
        #         min_list[idx] = prices[idx]
        #     else:
        #         min_list[idx] = min_list[idx - 1]

        # for idx in xrange(len_prices - 2, -1, -1):
        #     if prices[idx] > max_list[idx + 1]:
        #         max_list[idx] = prices[idx]
        #     else:
        #         max_list[idx] = max_list[idx + 1]

        # res = 0
        # for min_elem, max_elem in zip(min_list, max_list):
        #     res = max(res, max_elem - min_elem)

        # return res


sol = Solution()
# prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
print sol.maxProfit(prices)
