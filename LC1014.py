class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = curr_max = 0
        
        for idx in range(1, len(A)):
            curr_max = max(curr_max, A[idx] + idx)
            res = max(res, A[idx] - idx + curr_max)

        return res - 1


sol = Solution()
a = [8,1,5,2,6]
# a = [2,2,1]
# a = [1,2,2]
print(sol.maxScoreSightseeingPair(a))
