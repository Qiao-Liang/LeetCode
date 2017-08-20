class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edge_dict = {}  # Tracks the counts of each edge

        for row in wall:
            edge = 0
            for brick in row[: -1]:
                edge += brick

                if edge in edge_dict:
                    edge_dict[edge] += 1
                else:
                    edge_dict[edge] = 1
        
        max_edges = 0

        for key in edge_dict:
            if edge_dict[key] > max_edges:
                max_edges = edge_dict[key]
        
        return len(wall) - max_edges

sol = Solution()
wall = [[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
print(sol.leastBricks(wall))
