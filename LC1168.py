class Solution:
    def minCostToSupplyWater(self, n: int, wells, pipes) -> int:
        sets = [i for i in range(n + 1)]
        pipes += [[0, i, c] for i, c in enumerate(wells, 1)]
        res = 0

        def find(x):
            if x != sets[x]:
                sets[x] = find(sets[x])

            return sets[x]

        for u, v, w in sorted(pipes, key=lambda p: p[2]):
            x, y = find(u), find(v)

            if x != y:
                sets[x] = y
                res += w
                n -= 1

            if n == 0:
                return res

        # res = 0
        # sets = [i for i in range(n)]
        # watered = [False] * n
        # well_cost = [0] * n

        # def find(x):
        #     if x != sets[x]:
        #         sets[x] = find(sets[x])

        #     return sets[x]

        # for u, v, w in sorted(pipes, key=lambda p: p[2]):
        #     x, y = find(u - 1), find(v - 1)

        #     if watered[x] and watered[y]:
        #         continue
        #     else:
        #         if watered[x]:
        #             if wells[y] < w:
        #                 res += wells[y]
        #                 well_cost[y] = wells[y]
        #             else:
        #                 sets[y] = x
        #                 res += w

        #                 if wells[y] < well_cost[x]:
        #                     res -= well_cost[x]
        #                     res += wells[y]
        #                     well_cost = wells[y]
        #         elif watered[y]:
        #             if wells[x] < w:
        #                 res += wells[x]
        #                 well_cost[x] = wells[x]
        #             else:
        #                 sets[x] = y
        #                 res += w

        #                 if wells[x] < well_cost[y]:
        #                     res -= well_cost[y]
        #                     res += wells[x]
        #                     well_cost = wells[x]
        #         else:
        #             if wells[x] < wells[y]:
        #                 sets[y] = x
        #                 res += wells[x]
        #                 well_cost[x] = wells[x]
        #             else:
        #                 sets[x] = y
        #                 res += wells[y]
        #                 well_cost[y] = wells[y]

        #             res += w
                
        #         watered[x] = True
        #         watered[y] = True

        # for i in range(n):
        #     if not watered[i]:
        #         res += wells[i]

        # return res


sol = Solution()
# p = [3, [1,2,2], [[1,2,1],[2,3,1]]]
# p = [5,[46012,72474,64965,751,33304],[[2,1,6719],[3,2,75312],[5,3,44918]]]
p = [8,[24465,60420,69359,811,4421,52855,82734,86656],[[2,1,69860],[3,2,87910],[5,4,30690],[6,4,29178],[7,5,6800],[8,3,16250]]]
print(sol.minCostToSupplyWater(*p))
