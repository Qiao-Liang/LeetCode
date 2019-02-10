class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        stat = [0] * (N + 1)

        for dis in dislikes:
            stat[dis[0]] += 1
            stat[dis[1]] += 1

        # for cnt in stat[1:]:
        #     if cnt < 2:
        #         return True

        return sum([1 for n in stat if n == 2]) < 3


sol = Solution()
N = 4
dislikes = [[1,2],[1,3],[2,4]]

# N = 3
# dislikes = [[1,2],[1,3],[2,3]]

# N = 5
# dislikes = [[1,2],[3,4],[4,5],[3,5]]

print(sol.possibleBipartition(N, dislikes))
        