from collections import defaultdict

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_a = len(A)
        res = 0
        memo = defaultdict(int)
        
        for idx in range(1, len_a):
            for last_idx in range(idx):
                diff = A[idx] - A[last_idx]
                temp = max(memo[diff, idx], memo[diff, last_idx] + 1)
                res = max(temp, res)
                memo[diff, idx] = temp

        return res + 1


sol = Solution()
a = [3,6,9,12]
# a = [20,1,15,3,10,5,8]
# a = [83,20,17,43,52,78,68,45]
# a = [22,8,57,41,36,46,42,28,42,14,9,43,27,51,0,0,38,50,31,60,29,31,20,23,37,53,27,1,47,42,28,31,10,35,39,12,15,6,35,31,45,21,30,19,5,5,4,18,38,51,10,7,20,38,28,53,15,55,60,56,43,48,34,53,54,55,14,9,56,52]
print(sol.longestArithSeqLength(a))
