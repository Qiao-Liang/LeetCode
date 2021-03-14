from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        queue = [(K, 0)]
        visited = set([K])
        g = defaultdict(list)
        delay = [float('inf')] * (N + 1)
        delay[0] = delay[K] = 0
        
        for u, v, w in times:
            g[u].append((v, w))
        
        while queue:
            temp = []

            for n, d in queue:
                for tn, td in g[n]:
                    td += d

                    if tn not in visited or td < delay[tn]:
                        visited.add(tn)
                        delay[tn] = td
                        temp.append((tn, td))
            
            queue = temp
        
        return max(delay) if len(visited) == N else -1

    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        g = defaultdict(list)
        pq = [(0, K)]
        delay = {}

        for u, v, w in times:
            g[u].append((v, w))

        while pq:
            d, n = heappop(pq)

            if n not in delay:
                delay[n] = d

                for nei, nd in g[n]:
                    if nei not in delay:
                        heappush(pq, (d + nd, nei))
        
        return max(delay.values()) if len(delay) == N else -1


sol = Solution()
# params = [[[2,1,1],[2,3,1],[3,4,1]], 4, 2]
# params = [[[1,2,1],[2,3,2],[1,3,4]],3,1]
params = [[[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],5,3]
print(sol.networkDelayTime2(*params))
