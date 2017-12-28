class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        len_cost = len(cost)

        if len_cost < 3:
            return 0

        poss_cost = [0] * (len_cost + 1)

        for idx in range(2, len_cost + 1):
            poss_cost[idx] = min(poss_cost[idx - 1] + cost[idx - 1], poss_cost[idx - 2] + cost[idx - 2])
            
        return poss_cost[-1]


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [10, 15, 20]
sol = Solution()
print(sol.minCostClimbingStairs(cost))
