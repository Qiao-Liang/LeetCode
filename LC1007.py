from collections import defaultdict

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dic_A = defaultdict(set)
        dic_B = defaultdict(set)
        res = len_dom = len(A)

        for idx in range(len_dom):
            dic_A[A[idx]].add(idx)
            dic_B[B[idx]].add(idx)

        for key in dic_A:
            if len(dic_A[key] | dic_B[key]) == len_dom:
                res = min(res, min(len(dic_A[key]), len(dic_B[key])) - len(dic_A[key] & dic_B[key]))

        return res if res < len_dom else -1


sol = Solution()
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
# A = [3,5,1,2,3]
# B = [3,6,3,3,4]
print(sol.minDominoRotations(A, B))
