from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections):
        g = defaultdict(list)
        res = []
        [root_seq, parent] = [[n] * n for _ in range(2)]
        visited = [False] * n
        seq = 0

        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        def dfs(u):
            nonlocal seq
            visited[u] = True
            curr_seq = root_seq[u] = seq
            seq += 1

            for v in g[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)

                    if root_seq[v] > curr_seq:
                        res.append([u, v])

                if parent[u] != v:
                    root_seq[u] = min(root_seq[u], root_seq[v])

        dfs(0)
        return res

        # if len(g[0]) > 1:
        #     single[0] = False

        # def dfs(p, u, visited):
        #     for v in g[u]:
        #         if v in visited:
        #             if v != p:
        #                 single[u] = single[v] = False
        #         else:
        #             visited.add(v)
        #             dfs(u, v, visited)

        # dfs(-1, 0, set([0]))

        # for i, b in enumerate(single):
        #     if b:
        #         res.append([i, g[i][0]])

        # return res


sol = Solution()
p = [5, [[0,1],[1,2],[2,0],[1,3],[3,4]]]
print(sol.criticalConnections(*p))
