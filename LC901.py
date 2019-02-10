class StockSpanner:

    def __init__(self):
        self.prices = [float('inf')]
        self.spans = [1]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        idx = len(self.prices) - 1

        while idx > -1 and price >= self.prices[idx]:
            span += self.spans[idx]
            idx -= self.spans[idx]

        self.prices.append(price)
        self.spans.append(span)
        
        return span

        # if price < self.price_stack[-1]:
        #     self.price_stack.append(price)
        #     return 1
        # else:
        #     temp_stack = []
        #     count = 1

        #     while self.price_stack[-1] < price:
        #         temp_stack.append(self.price_stack.pop())
        #         count += 1

        #     self.price_stack.append(price)
        #     self.price_stack.extend(temp_stack)
        #     return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

obj = StockSpanner()
# 100, 80, 60, 70, 60, 75, 85

# [[],[29],[91],[62],[76],[51]]

print(obj.next(29))
print(obj.next(91))
print(obj.next(62))
print(obj.next(76))
print(obj.next(51))
