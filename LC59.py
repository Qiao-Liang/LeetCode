class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        curr_num = 1
        bound = n * n
        size = n
        layer = 0
        res = [[0] * n for _ in xrange(n)]

        while True:
            col = layer
            row = layer
            count = 0

            while count < size:
                res[row][col] = curr_num
                curr_num += 1
                col += 1
                count += 1

            if curr_num > bound:
                break

            row = layer + 1
            col = n - layer - 1
            count = 2

            while count < size:
                res[row][col] = curr_num
                curr_num += 1
                row += 1
                count += 1

            if curr_num > bound:
                break

            row = n - layer - 1
            col = n - layer - 1
            count = 0

            while count < size:
                res[row][col] = curr_num
                curr_num += 1
                col -= 1
                count += 1
            
            if curr_num > bound:
                break

            row = n - layer - 2
            col = layer
            count = 2

            while count < size:
                res[row][col] = curr_num
                curr_num += 1
                row -= 1
                count += 1

            if curr_num > bound:
                break

            layer += 1
            size -= 2

        return res


sol = Solution()
print sol.generateMatrix(4)
