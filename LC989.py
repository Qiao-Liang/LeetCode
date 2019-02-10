class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        
        return [int(s) for s in str(int(''.join(map(str, A))) + K)]


sol = Solution()
A = [1,2,0,0]
K = 34
print(sol.addToArrayForm(A, K))
