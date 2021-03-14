class Solution:
    def isBipartite(self, graph):
        def bfs(n, g, c):
            q = [n]
            c[n] = 0

            for k in q:
                for n in g[k]:
                    if c[n] == c[k]:
                        return True
                    
                    if c[n] == None:
                        c[n] = not c[k]
                        q.append(n)
            
            return False

        c = [None] * len(graph)
        
        for i in range(len(graph)):
            if c[i] == None and bfs(i, graph, c):
                return False
        
        return True


        # s = [set([]), set([])]
        # i = 0
        # q = []

        # for u, vs in enumerate(graph):
        #     if vs:
        #         q.append(u)
        #         s[i].add(u)
        #         break

        # while q:
        #     tq = []
        #     ni = (i + 1) % 2

        #     for k in q:
        #         for n in graph[k]:
        #             if n not in s[i] and n not in s[ni]:
        #                 s[ni].add(n)
        #                 tq.append(n)

        #     i = ni
        #     q = tq
        
        # for u, vs in enumerate(graph):
        #     for v in vs:
        #         if u in s[0] and v in s[0] or v in s[1] and u in s[1]:
        #             return False

        # return True


sol = Solution()
g = [[1,3],[0,2],[1,3],[0,2]]
# g = [[1,2,3], [0,2], [0,1,3], [0,2]]
# g = [[1,4],[0,2],[1],[4],[0,3]]
# g = [[1], [0, 2], [1, 3], [2, 4], [3]]
# g = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
# g = [[],[3],[],[1],[]]
# g = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
print(sol.isBipartite(g))
