from collections import Counter

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        temp1 = temp2 = 0
        
        for o_idx, o_row in enumerate(matrix):
            for i_row in matrix[o_idx + 1:]:
                temp = []
                
                for o_n, i_n in zip(o_row, i_row):
                    temp.append(o_n ^ i_n)
                    
                counter = Counter(temp)
                
                if counter[0] == 0 or counter[1] == 0:
                    temp1 += 2
                else:
                    temp2 += 1
        
        return max(temp1, temp2)


sol = Solution()
# m = [[0,1],[1,1]]
# m = [[0,1],[1,0]]
# m = [[0,0,0],[0,0,1],[1,1,0]]
m = [
    [1,0,0,0,1,1,1,0,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0],
    [1,0,0,0,1,1,1,0,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0],
    [1,1,1,0,1,1,1,0,1,1,1]]
print(sol.maxEqualRowsAfterFlips(m))
