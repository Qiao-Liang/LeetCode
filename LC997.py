from collections import defaultdict

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            return 1 if N == 1 else -1

        be_trusted = defaultdict(list)
        trusting = set([])

        for a, b in trust:
            be_trusted[b].append(a)
            trusting.add(a)

        for judge, others in be_trusted.items():
            if judge not in trusting and len(others) == N - 1:
                return judge

        return -1


sol = Solution()
# N = 2
# trust = [[1,2]]
N = 1
trust = []
print(sol.findJudge(N, trust))
