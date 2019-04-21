class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        len_a = len(A)
        flipped = [0] * len_a
        res = flip = 0

        for i, n in enumerate(A):
            flip ^= flipped[i]

            if n == flip:
                if i + K > len_a:
                    return -1

                res += 1
                flip ^= 1

                if i + K < len_a:
                    flipped[i + K] ^= 1

        return res

        # if K == 1:
        #     count = 0

        #     for n in A:
        #         if n == 0:
        #             count += 1

        #     return count

        # target = 0
        # idx = 0
        # bound = len(A)
        # res = 0

        # while idx < bound:
        #     if A[idx] == target:
        #         count = 0
        #         res += 1

        #         while count < K and A[idx] == target:
        #             idx += 1
        #             count += 1

        #         if count < K:
        #             target ^= 1
        #             idx -= 1

        #         if bound - idx < K:
        #             return -1
        #         elif bound - idx == K:
        #             for n in A[idx:]:
        #                 if n != target:
        #                     return -1
                    
        #             return res
        #         else:
        #             continue
        #     else:
        #         idx += 1


sol = Solution()
# A = [1,1,1,1,0]
# K = 2
A = [0,0,0,1,0,1,1,0]
K = 3
print(sol.minKBitFlips(A, K))
