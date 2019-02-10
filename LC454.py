class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        res = 0

        for a in A:
            for b in B:
                temp = a + b

                if temp in dic:
                    dic[temp] += 1
                else:
                    dic[temp] = 1

        for c in C:
            for d in D:
                res += dic.get(-(c + d), 0)

        return res

        # if not A:
        #     return 0

        # dic1 = {}
        # dic2 = {}
        # res = 0
        # bound = len(A)

        # for idx1 in range(bound):
        #     for idx2 in range(bound):
        #         temp1 = A[idx1] + B[idx2]
        #         temp2 = C[idx1] + D[idx2]

        #         if temp1 in dic1:
        #             dic1[temp1] += 1
        #         else:
        #             dic1[temp1] = 1

        #         if temp2 in dic2:
        #             dic2[temp2] += 1
        #         else:
        #             dic2[temp2] = 1

        # for key, val in dic1.items():
        #     if -key in dic2:
        #         res += val * dic2[-key]

        # return res


sol = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

# A = []
# B = []
# C = []
# D = []

print(sol.fourSumCount(A, B, C, D))
