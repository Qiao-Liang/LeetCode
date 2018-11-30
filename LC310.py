class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 2:
            return [0]

        deg_list = [0] * n
        adj_map = [[] for _ in xrange(n)]

        for edge in edges:
            deg_list[edge[0]] += 1
            deg_list[edge[1]] += 1
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])

        queue = [node for node in xrange(n) if deg_list[node] == 1]

        while queue:
            temp_queue = []

            for node in queue:
                for neigh in adj_map[node]:
                    deg_list[neigh] -= 1
                    
                    if deg_list[neigh] == 1:
                        temp_queue.append(neigh)

            if temp_queue:           
                queue = temp_queue
            else:
                return queue

        # if not edges:
        #     return [0]

        # dist = [[None] * n for _ in xrange(n)]

        # for edge in edges:
        #     dist[edge[0]][edge[1]] = 1
        #     dist[edge[1]][edge[0]] = 1

        # for srt in xrange(n):
        #     for end in xrange(n):
        #         if not dist[srt][end] and srt != end:
        #             min_dist = None

        #             for mid in xrange(n):
        #                 if mid != srt and mid != end and dist[srt][mid] and dist[mid][end]:
        #                     if min_dist:
        #                         min_dist = min(min_dist, dist[srt][mid] + dist[mid][end])
        #                     else:
        #                         min_dist = dist[srt][mid] + dist[mid][end]

        #             dist[srt][end] = min_dist

        # min_height = []

        # for idx, row in enumerate(dist):
        #     temp_height = max(row)

        #     if not min_height or temp_height < min_height[0]:
        #         min_height = [temp_height, [idx]]
        #     elif temp_height == min_height[0]:
        #         min_height[1].append(idx)

        # return min_height[1]

        
        # adj_map = {}
        # min_height = []

        # for edge in edges:
        #     if edge[0] in adj_map:
        #         adj_map[edge[0]].append(edge[1])
        #     else:
        #         adj_map[edge[0]] = [edge[1]]

        #     if edge[1] in adj_map:
        #         adj_map[edge[1]].append(edge[0])
        #     else:
        #         adj_map[edge[1]] = [edge[0]]

        # for num in xrange(n):
        #     queue = [num]
        #     temp_height = 0
        #     visited = set([num])

        #     while queue:
        #         temp_queue = []

        #         for node in queue:
        #             for neigh in adj_map[node]:
        #                 if neigh not in visited:
        #                     temp_queue.append(neigh)
        #                     visited.add(neigh)

        #         queue = temp_queue
        #         temp_height += 1

        #     if not min_height or temp_height < min_height[0]:
        #         min_height = [temp_height, [num]]
        #     elif temp_height == min_height[0]:
        #         min_height[1].append(num)

        # return min_height[1]


sol = Solution()
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
# n = 6
# edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print sol.findMinHeightTrees(n, edges)
