class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or numRows >= len(s):
            return s

        # arrays = [[] for _ in range(numRows)]
        # row = 0
        # down = True

        # for c in s:
        #     arrays[row].append(c)

        #     if down:
        #         row += 1
        #     else:
        #         row -= 1

        #     if row == -1:
        #         row = 1
        #         down = True
            
        #     if row == numRows:
        #         row = numRows - 2
        #         down = False

        # return ''.join([''.join(array) for array in arrays])

        arr = [''] * numRows
        row = 0
        step = 1
        limit = numRows - 1

        for c in s:
            arr[row] += c

            if row == limit:
                step = -1
            elif row == 0:
                step = 1

            row += step

        return ''.join(arr)


sol = Solution()
print(sol.convert('PAYPALISHIRING', 3))