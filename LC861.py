class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        res = 0

        for c in range(cols):
            col = 0

            for r in range(rows):
                col += A[r][c] ^ A[r][0]
            
            res += max(col, rows - col) * (1 << (cols - c - 1))

        return res


sol = Solution()
a = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(sol.matrixScore(a))
