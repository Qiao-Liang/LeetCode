class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses or not prerequisites:
            return True

        in_degs = [0] * numCourses
        adj_map = [[] for _ in xrange(numCourses)]
        zero_degs = []

        for pair in prerequisites:
            adj_map[pair[1]].append(pair[0])
            in_degs[pair[0]] += 1

        for idx, val in enumerate(in_degs):
            if val == 0:
                zero_degs.append(idx)

        while zero_degs:
            temp = zero_degs.pop()

            for neigh in adj_map[temp]:
                in_degs[neigh] -= 1

                if in_degs[neigh] == 0:
                    zero_degs.append(neigh)

        return all([deg == 0 for deg in in_degs])


sol = Solution()
nums = 2
# pres = [[1,0],[0,1]]
pres = [[1,0]]
print sol.canFinish(nums, pres)
