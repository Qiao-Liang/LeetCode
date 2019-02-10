class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = {}
        res = []

        def dfs(curr, target, temp):
            nonlocal dic, visited, temp_res
            curr_item = dic[curr]

            if target in curr_item:
                temp_res = temp * curr_item[target]
            else:
                for key, val in curr_item.items():
                    if key not in visited:
                        visited.add(key)
                        dfs(key, target, temp * val)

        for (x, y), val in zip(equations, values):
            if x in dic:
                dic[x][y] = val
            else:
                dic[x] = {y: val}

            val = 1 / val
            if y in dic:
                dic[y][x] = val
            else:
                dic[y] = {x: val}

        for x, y in queries:
            if y == 0 or x not in dic or y not in dic:
                res.append(-1.0)
            elif x == 0:
                res.append(0)
            elif x == y:
                res.append(1.0)
            else:
                if y in dic[x]:
                    res.append(dic[x][y])
                else:
                    visited = set([])
                    temp_res = -1.0
                    dfs(x, y, 1.0)
                    res.append(temp_res)

                    # not_found = True

                    # for key in dic[x]:
                    #     if y in dic[key]:
                    #         res.append(dic[x][key] * dic[key][y])
                    #         not_found = False
                    
                    # if not_found:
                    #     res.append(-1.0)

        return res


e = [ ["a", "b"], ["b", "c"] ]
v = [2.0, 3.0]
q = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
sol = Solution()

# e = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
# v = [3.0,4.0,5.0,6.0]
# q = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

print(sol.calcEquation(e, v, q))
