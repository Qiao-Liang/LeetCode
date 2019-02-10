class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.nums = A
        self.bound = len(A) - 1
        self.res = sum([row[0] for row in A])

        def recurse(row, col, temp):
            if row == self.bound:
                self.res = min(self.res, temp + self.nums[row][col])
            else:
                temp_sum = temp + self.nums[row][col]
                row += 1

                if col > 0:
                    recurse(row, col - 1, temp_sum)

                recurse(row, col, temp_sum)

                if col < self.bound:
                    recurse(row, col + 1, temp_sum)

        for col in range(len(A)):
            recurse(0, col, 0)

        return self.res


sol = Solution()
a = [[1,2,3],[4,5,6],[7,8,9]]
# a = [[-19,57],[-40,-5]]
print(sol.minFallingPathSum(a))
        