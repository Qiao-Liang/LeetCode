class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)

        def merge_sort(temp_nums):
            if not temp_nums:
                return []

            len_nums = len(temp_nums)
            
            if len_nums == 1:
                return temp_nums

            mid = len_nums // 2

            left = merge_sort(temp_nums[:mid])
            right = merge_sort(temp_nums[mid:])
            len_left = len(left)
            len_right = len(right)
            idx_left = idx_right = 0
            temp_res = []

            while idx_left < len_left and idx_right < len_right:
                if left[idx_left][0] < right[idx_right][0]:
                    temp_res.append(left[idx_left])
                    idx_left += 1
                elif left[idx_left][0] > right[idx_right][0]:
                    for _, idx in left[idx_left:]:
                        res[idx] += 1
                    
                    temp_res.append(right[idx_right])
                    idx_right += 1
                else:
                    temp_res.extend([left[idx_left], right[idx_right]])
                    idx_left += 1
                    idx_right += 1

            if idx_left < len_left:
                temp_res.extend(left[idx_left:])
            
            if idx_right < len_right:
                temp_res.extend(right[idx_right:])

            return temp_res

        merge_sort([(num, idx) for idx, num in enumerate(nums)])
        return res


sol = Solution()
# nums = [5,2,6,1]
nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
print(sol.countSmaller(nums))
