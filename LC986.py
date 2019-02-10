# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        idx_a = idx_b = 0
        len_a = len(A)
        len_b = len(B)

        while idx_a < len_a and idx_b < len_b:
            start = max(A[idx_a].start, B[idx_b].start)
            end = min(A[idx_a].end, B[idx_b].end)

            if start <= end:
                res.append(Interval(start, end))
            
            if A[idx_a].end < B[idx_b].end:
                idx_a += 1
            else:
                idx_b += 1

        return res


        # if not A or not B:
        #     return []

        # len_a = len(A)
        # len_b = len(B)
        # idx_a = idx_b = 0
        # res = []

        # while idx_a < len_a and idx_b < len_b:
        #     if A[idx_a].end < B[idx_b].start:
        #         idx_a += 1
        #     elif A[idx_a].start > B[idx_b].end:
        #         idx_b += 1
        #     else:
        #         res.append(Interval(max(A[idx_a].start, B[idx_b].start), min(A[idx_a].end, B[idx_b].end)))

        #         if A[idx_a].end - A[idx_b].start > B[idx_b].end - B[idx_b].start:
        #             idx_b += 1
        #         elif A[idx_a].end - A[idx_b].start < B[idx_b].end - B[idx_b].start:
        #             idx_a += 1
        #         else:
        #             idx_a += 1
        #             idx_b += 1

        # return res


sol = Solution()
# A = [Interval(0,2),Interval(5,10),Interval(13,23),Interval(24,25)]
# B = [Interval(1,5),Interval(8,12),Interval(15,24),Interval(25,26)]
A = [[0,4],[7,8],[12,19]]
B = [[0,10],[14,15],[18,20]]
A = [Interval(n[0], n[1]) for n in A]
B = [Interval(n[0], n[1]) for n in B]
res = sol.intervalIntersection(A, B)

print([[obj.start, obj.end] for obj in res])

