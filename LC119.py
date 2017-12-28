class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            result = [1, 1]
            count = 1

            while count < rowIndex:
                temp = [1]

                for idx in range(len(result) - 1):
                    temp.append(result[idx] + result[idx + 1])

                temp.append(1)
                result = temp
                count += 1

        return result


sol = Solution()
print(sol.getRow(3))
