class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[], [nums[0]]]
        add_len = 1

        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                result.extend([elem + [nums[idx]] for elem in result[-add_len:]])
            else:
                add_len = len(result)
                result.extend([elem + [nums[idx]] for elem in result])

        return result


sol = Solution()
# nums = [1, 2, 2, 3, 3]
nums = [1, 1, 2]
print(sol.subsetsWithDup(nums))
