from bisect import bisect

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_a = len(A)
        res = 0
        cands = [(A[-1], len_a - 1)]
        
        for i in range(len_a - 2, -1, -1):
            bi = bisect(cands, (A[i], i))
            
            if bi < len(cands):
                res = max(res, cands[bi][1] - i)
            else:
                cands.append((A[i], i))
        
        return res

        # temp = sorted([n for n in range(len(A))], key=lambda n: A[n])
        # min_idx = temp[0]
        # res = 0
        
        # for idx in temp[1:]:
        #     min_idx = min(min_idx, idx)
        #     res = max(res, idx - min_idx)
        
        # return res

        # temp = [(num, idx) for idx, num in enumerate(A)]
        # temp.sort(key=lambda n: n[0])
        # min_idx = temp[0][1]
        # res = 0
        
        # for _, idx in temp[1:]:
        #     min_idx = min(min_idx, idx)
        #     res = max(res, idx - min_idx)
        
        # return res


sol = Solution()
a = [6,0,8,2,1,5]
print(sol.maxWidthRamp(a))
