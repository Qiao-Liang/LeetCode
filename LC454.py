class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0

        for a in A:
            for b in B:
                for c in C:
                    for d in D:
                        if a + b + c + d == 0:

        