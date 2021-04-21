class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = emptyBottles = numBottles
        
        while emptyBottles >= numExchange:
            fullBottles = emptyBottles // numExchange
            res += fullBottles
            emptyBottles = fullBottles + emptyBottles % numExchange
        
        return res


sol = Solution()
n, e = 15, 4
print(sol.numWaterBottles(n, e))
