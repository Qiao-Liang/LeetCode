from functools import lru_cache
from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        len_arr1 = len(arr1)
        len_arr2 = len(arr2)
        arr2.sort()
        MAX_VAL = float('inf')

        @lru_cache(None)
        def recurse(i, curr):
            if i >= len_arr1:
                return 0

            ri = bisect_right(arr2, curr)
            return min(1 + recurse(i + 1, arr2[ri]) if ri < len_arr2 else MAX_VAL,
                        recurse(i + 1, arr1[i]) if arr1[i] > curr else MAX_VAL)

        res = recurse(0, -MAX_VAL)
        return res if res != MAX_VAL else -1


        # arr2.sort()
        # self.res = float('inf')
        # len_arr1 = len(arr1)
        # len_arr2 = len(arr2)

        # def dfs(arr, srt, ops):
        #     is_sorted = True

        #     for i in range(srt, len_arr1):
        #         last = arr[i - 1]
        #         curr = arr[i]

        #         if arr[i] <= last:
        #             is_sorted = False
        #             li = bisect_left(arr2, last)
        #             ci = bisect_right(arr2, curr)

        #             if li < len_arr2:
        #                 arr[i] = arr2[li]
        #                 dfs(arr, i + 1, ops + 1)
        #                 arr[i] = curr

        #             if ci > 0:
        #                 if arr2[ci] == curr:
        #                     arr[i - 1] = arr2[ci]
        #                 else:
        #                     arr[i - 1] = arr2[ci - 1]
                        
        #                 dfs(arr, i, ops + 1)
        #                 arr[i - 1] = last
            
        #     if is_sorted:
        #         self.res = min(self.res, ops)

        # dfs(arr1, 1, 0) 
        # return self.res
        # return self.res if self.res < float('int') else -1


sol = Solution()
# arr1 = [1,5,3,6,7]
# arr2 = [1,3,2,4]
arr1 = [1,5,3,6,7]
arr2 = [4,3,1]
print(sol.makeArrayIncreasing(arr1, arr2))
