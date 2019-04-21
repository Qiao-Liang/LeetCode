class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        start = res = 0

        for end in range(len(A)):
            K -= A[end] == 0

            if K < 0:
                K += A[start] == 0
                start += 1

            res = end - start + 1

            # while K < 0:
            #     K += A[start] == 0
            #     start += 1

            # res = max(res, end - start + 1)

        return res

        # start = end = 0
        # len_A = len(A)
        # zeros = 0
        # res = 0

        # while end < len_A:
        #     while end < len_A and zeros <= K:
        #         zeros += A[end] == 0
        #         end += 1

        #     res = max(res, end - start - (zeros > K))

        #     while start <= end and zeros > K:
        #         zeros -= A[start] == 0
        #         start += 1

        # return res


sol = Solution()
# A = [1]
# K = 2
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
# A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# K = 3
# A = [1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1]
# K = 8
# A = [0,0,1,1,1,0,0]
# K = 0
# A = [0, 0, 0, 0]
# K = 0
print(sol.longestOnes(A, K))
