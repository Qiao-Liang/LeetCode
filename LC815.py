from collections import defaultdict

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        buses = [set(route) for route in routes]
        graph = defaultdict(set)
        len_routes = len(routes)
        res = float('inf')

        for idx0 in range(len_routes):
            for idx1 in range(idx0 + 1, len_routes):
                if buses[idx0] & buses[idx1]:
                    graph[idx0].add(idx1)
                    graph[idx1].add(idx0)

        for idx, bus in enumerate(buses):
            if S in bus:
                queue = [idx]
                count = 0
                visited = set()
                done = False

                while queue:
                    temp_queue = []
                    count += 1

                    for bus_idx in queue:
                        if T in buses[bus_idx]:
                            done = True
                            break

                        for next_bus_idx in graph[bus_idx]:
                            if next_bus_idx not in visited:
                                visited.add(next_bus_idx)
                                temp_queue.append(next_bus_idx)
                    
                    if done:
                        break
                    else:
                        queue = temp_queue
            
                if done:
                    res = min(res, count)

        return res if res != float('inf') else -1


sol = Solution()
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
print(sol.numBusesToDestination(routes, S, T))
