class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        srt = curr = 0
        end = len(nums) - 1

        while curr <= end:
            if nums[curr] == 0:
                nums[curr], nums[srt] = nums[srt], nums[curr]
                srt += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1

        return nums

sol = Solution()

nums = [0, 1, 1, 2, 0, 0, 2, 1, 1, 2, 2, 0]
# nums = [1, 0]
print(sol.sortColors(nums))
