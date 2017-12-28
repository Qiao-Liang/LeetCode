class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            nums = nums[::-1]
        else:
            nums[:k + 1] = nums[:k + 1][::-1]
            nums[k + 1:] = nums[k + 1:][::-1]
            nums = nums[::-1]

        print(nums)


sol = Solution()
sol.rotate([1, 2], 3)
