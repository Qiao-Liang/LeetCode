class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        bound = 0

        for idx in range(1, len(nums)):
            if nums[idx] != nums[bound]:
                bound += 1
                nums[bound] = nums[idx]

        return bound + 1


        # if not nums:
        #     return 0

        # new_len = 1
        # step = 0

        # for idx in range(1, len(nums)):
        #     if nums[idx] == nums[idx - 1]:
        #         step += 1
        #     else:
        #         nums[idx - step] = nums[idx]
        #         new_len += 1

        # nums = nums[:new_len]

        # return new_len

sol = Solution()
print(sol.removeDuplicates([1, 1, 1, 2, 2, 3, 4]))
