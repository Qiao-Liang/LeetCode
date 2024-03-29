from collections import Counter

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lamp_set = set([(x, y) for x, y in lamps])
        res = [0] * len(queries)
        dic_x = Counter()
        dic_y = Counter()
        dic_xy = Counter()
        dic_yx = Counter()

        for x, y in lamps:
            dic_x[x] += 1
            dic_y[y] += 1
            dic_xy[x - y] += 1
            dic_yx[x + y] += 1

        for idx, (x, y) in enumerate(queries):
            xy = x - y
            yx = x + y

            if x in dic_x and dic_x[x] or y in dic_y and dic_y[y] or xy in dic_xy and dic_xy[xy] or yx in dic_yx and dic_yx[yx]:
                res[idx] = 1
            
            for lamp_x, lamp_y in [(x, y), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1)]:
                if (lamp_x, lamp_y) in lamp_set:
                    dic_x[lamp_x] -= 1
                    dic_y[lamp_y] -= 1
                    dic_xy[lamp_x - lamp_y] -= 1
                    dic_yx[lamp_x + lamp_y] -= 1

        return res


        # cells = [[0] * N for _ in range(N)]
        # res = [0] * len(queries)
        # lamp_set = set([])

        # def switch(x, y, delta):
        #     for idx in range(N):
        #         cells[idx][y] += delta
        #         cells[x][idx] += delta

        #     cells[x][y] -= delta

        #     temp_x = x - 1
        #     temp_y = y - 1

        #     while temp_x > -1 and temp_y > -1:
        #         cells[temp_x][temp_y] += delta
        #         temp_x -= 1
        #         temp_y -= 1

        #     temp_x = x + 1
        #     temp_y = y + 1

        #     while temp_x < N and temp_y < N:
        #         cells[temp_x][temp_y] += delta
        #         temp_x += 1
        #         temp_y += 1

        #     temp_x = x - 1
        #     temp_y = y + 1

        #     while temp_x > -1 and temp_y < N:
        #         cells[temp_x][temp_y] += delta
        #         temp_x -= 1
        #         temp_y += 1

        #     temp_x = x + 1
        #     temp_y = y - 1

        #     while temp_x < N and temp_y > -1:
        #         cells[temp_x][temp_y] += delta
        #         temp_x += 1
        #         temp_y -= 1

        # for x, y in lamps:
        #     switch(x, y, 1)
        #     lamp_set.add((x, y))

        # for idx, (x, y) in enumerate(queries):
        #     if cells[x][y] != 0:
        #         res[idx] = 1

        #     for temp_x, temp_y in [(x, y), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1)]:
        #         if (temp_x, temp_y) in lamp_set:
        #             switch(temp_x, temp_y, -1)

        # return res


sol = Solution()
# N = 5
# lamps = [[0,0],[4,4]]
# queries = [[1,1],[1,0]]
# N = 5
# lamps = [[0,0],[4,4]]
# queries = [[1,1],[1,1]]

N = 100
lamps = [[7,55],[53,61],[2,82],[67,85],[81,75],[38,91],[68,0],[60,43],[40,19],[12,75],[26,2],[24,89],[42,81],[60,58],[77,72],[33,24],[19,93],[7,16],[58,54],[78,57],[97,49],[65,16],[42,75],[90,50],[89,34],[76,97],[58,23],[62,47],[94,28],[88,65],[3,87],[81,10],[12,81],[44,81],[54,92],[90,54],[17,54],[27,82],[48,15],[8,46],[4,99],[15,13],[90,77],[2,87],[18,33],[52,90],[4,95],[57,61],[31,22],[32,8],[49,26],[24,65],[88,55],[88,38],[64,76],[94,76],[59,12],[41,46],[80,28],[38,36],[65,67],[75,37],[56,97],[83,57],[2,4],[44,43],[71,90],[62,40],[79,94],[81,11],[96,34],[38,11],[22,3],[54,96],[78,33],[54,54],[79,98],[1,28],[0,32],[37,11]]
queries = [[24,84],[95,68],[80,35],[31,53],[69,45],[85,29],[87,25],[42,47],[7,59],[99,3],[31,70],[64,62],[44,91],[55,25],[15,52],[95,33],[21,29],[61,34],[93,34],[79,27],[30,86],[52,0],[18,10],[5,1],[40,21],[11,48],[55,94],[22,42],[81,0],[39,43],[5,25],[43,29],[45,47],[83,93],[77,70],[22,63],[30,73],[18,48],[39,88],[91,47]]

[1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]

print(sol.gridIllumination(N, lamps, queries))
