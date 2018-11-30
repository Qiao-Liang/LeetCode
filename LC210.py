class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_map = [[] for _ in range(numCourses)]
        in_degs = [0] * numCourses
        res = []
        srcs = []

        for prep in prerequisites:
            adj_map[prep[1]].append(prep[0])
            in_degs[prep[0]] += 1

        for idx, deg in enumerate(in_degs):
            if deg == 0:
                srcs.append(idx)

        while srcs:
            temp = srcs.pop()
            res.append(temp)

            for trgt in adj_map[temp]:
                in_degs[trgt] -= 1

                if in_degs[trgt] == 0:
                    srcs.append(trgt)

        return res if len(res) == numCourses else []


sol = Solution()
# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
num = 3
prep = [[1,0],[1,2],[0,1]]
print(sol.findOrder(num, prep))
