class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None

        for row in range(len(triangle) - 2, -1, -1):
            curr_row = triangle[row]
            last_row = triangle[row + 1]
            for col in range(row + 1):
                curr_row[col] = min(last_row[col], last_row[col + 1]) + curr_row[col]

        return triangle[0][0]


    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.min_val = sum([row[0] for row in triangle])
        self.last_row = len(triangle) - 1

        def dfs(row, col, temp_sum):
            temp_sum += triangle[row][col]

            if row == self.last_row:
                if temp_sum < self.min_val:
                    self.min_val = temp_sum
                
                return
            else:
                row += 1
                left = col
                right = col + 1
                
                dfs(row, left, temp_sum)
                dfs(row, right, temp_sum)

        dfs(0, 0, 0)

        return self.min_val


sol = Solution()
m = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
# m = [[-1], [-2, -3]]
print(sol.minimumTotal(m))
