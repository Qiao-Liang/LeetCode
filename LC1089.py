class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        len_arr = len(arr)
        idx = 0
        
        while idx < len_arr:
            if arr[idx] == 0:
                temp_idx = len_arr - 1

                while temp_idx > idx:
                    arr[temp_idx] = arr[temp_idx - 1]
                    temp_idx -= 1

                idx += 2
            else:
                idx += 1

        print(arr)


sol = Solution()
a = [1,0,2,3,0,4,5,0]
sol.duplicateZeros(a)
