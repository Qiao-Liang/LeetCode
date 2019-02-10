class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        len_nums = len(nums)
        nums_bound = len_nums - 1
        idx = 0

        while idx < nums_bound:
            res += 1
            bound = nums[idx] + idx

            if bound >= nums_bound:
                break

            temp_idx = max_idx = idx + 1
            max_range = nums[max_idx] + max_idx
            
            while temp_idx <= bound and temp_idx < len_nums:
                temp_range = nums[temp_idx] + temp_idx

                if temp_range >= max_range:
                    max_range = temp_range
                    max_idx = temp_idx

                temp_idx += 1

            idx = max_idx

        return res


sol = Solution()
nums = [2,3,1,1,4]
# nums = [3, 2, 1]
# nums = [1,2,1,1,1]
# nums = [10,9,8,7,6,5,4,3,2,1,1,0]
print(sol.jump(nums))
