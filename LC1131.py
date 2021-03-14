class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        res, len_arr = 0, len(arr1)

        for op1, op2 in ((-1, -1), (-1, 1), (1, 1), (1, -1)):
            closest = arr1[0] * op1 + arr2[0] * op2

            for i in range(len_arr):
                cur = arr1[i] * op1 + arr2[i] * op2 + i
                res = max(res, cur - closest)
                closest = min(closest, cur)
        
        return res

        # temp1 = sorted([(v, i) for i, v in enumerate(arr1)], key=lambda n: n[0])
        # temp2 = sorted([(v, i) for i, v in enumerate(arr2)], key=lambda n: n[0])
        # self.res = 0
        # len_arr = len(arr1)
        
        # def loop(temp, arr):
        #     l, r = 0, len_arr - 1

        #     while l < r:
        #         self.res = max(self.res, abs(temp[r][0] - temp[l][0]) + abs(arr[temp[r][1]] - arr[temp[l][1]]) + abs(temp[r][1] - temp[l][1]))

        #         if temp[l + 1][0] - temp[l][0] > temp[r][0] - temp[r - 1][0]:
        #             r -= 1
        #         else:
        #             l += 1
        
        # loop(temp1, arr2)
        # loop(temp2, arr1)
        # return self.res


sol = Solution()
arr1 = [-930921,182366,-715780,119677,517554,211959,-320500,-737078,890716,-242060,625048,-553970,-679460,-448085,133566,193789,726154,-984806,-253960,-351914,-937855,-817981,784169,747359,509712,485932,-622044,-18157,698899,-923616]
arr2 = [854632,428107,-704467,832706,-319640,-365224,-947863,729070,-312850,36528,311684,-100859,-177471,-558426,-661854,668679,-87676,-646544,30934,-349421,165215,-183902,417453,86953,388125,-797836,115123,156068,-479616,313614]
print(sol.maxAbsValExpr(arr1, arr2))
