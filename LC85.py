class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        heights.append(0)
        max_rec = 0
        min_stk = [0] * (len(heights) + 1)
        stk_ptr = 0
        min_stk[stk_ptr] = -1

        for idx, val in enumerate(heights):
            while val < heights[min_stk[stk_ptr]]:
                max_rec = max(max_rec, heights[min_stk[stk_ptr]] * (idx - min_stk[stk_ptr - 1] - 1))
                stk_ptr -= 1

            stk_ptr += 1
            min_stk[stk_ptr] = idx

        return max_rec

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        accu_rec = [0] * len(matrix[0])
        max_rec = 0

        for row in matrix:
            for idx in range(len(row)):
                if row[idx] == "0":
                    accu_rec[idx] = 0
                else:
                    accu_rec[idx] += 1

            max_rec = max(max_rec, self.largestRectangleArea(accu_rec))

        return max_rec


sol = Solution()

m = [["0","1","1","0","1"],
     ["1","1","0","1","0"],
     ["0","1","1","1","0"],
     ["1","1","1","1","0"],
     ["1","1","1","1","1"],
     ["0","0","0","0","0"]]

# m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(sol.maximalRectangle(m))
