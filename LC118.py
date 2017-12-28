class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            count = 2

            while count < numRows:
                last = result[-1]
                temp = [1]

                for idx in range(len(last) - 1):
                    temp.append(last[idx] + last[idx + 1])

                temp.append(1)
                result.append(temp)
                count += 1

        return result


sol = Solution()
print(sol.generate(5))
