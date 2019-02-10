class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda n: (n[0], n[1]))
        len_pairs = len(pairs)
        memo = [1] * len_pairs
        res = 0

        for left in range(len_pairs - 2, -1, -1):
            for right in range(left + 1, len_pairs):
                if pairs[left][1] < pairs[right][0]:
                    memo[left] = max(memo[left], memo[right] + 1)

            res = max(res, memo[left])
            
        return res


sol = Solution()
# p = [[1,2], [2,3], [3,4]]
# p = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
# p = [[-1,1],[-2,7],[-5,8],[-3,8],[1,3],[-2,9],[-5,2]]
p = [[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]]
print(sol.findLongestChain(p))
