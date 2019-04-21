class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda n: n[0] - n[1])
        bound = len(costs) // 2
        return sum([cost_a for cost_a, _ in costs[: bound]]) + sum([cost_b for _, cost_b in costs[bound:]])

        # costs.sort(key=lambda n: (n[0], n[1]))
        # count_a = count_b = len(costs) / 2
        # res = 0
        
        # for cost_a, cost_b in costs:
        #     if cost_a < cost_b:
        #         if count_a > 0:
        #             res += cost_a
        #             count_a -= 1
        #         else:
        #             res += cost_b
        #             count_b -= 1
        #     elif cost_a > cost_b:
        #         if count_b > 0:
        #             res += cost_b
        #             count_b -= 1
        #         else:
        #             res += cost_a
        #             count_a -= 1
        #     else:
        #         if count_a > count_b:
        #             res += cost_b
        #             count_b -= 1
        #         else:
        #             res += count_a
        #             count_a -= 1
        
        # return res


sol = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
print(sol.twoCitySchedCost(costs))
