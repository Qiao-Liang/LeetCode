class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        start = 0
        end = length - 1
        pivot = -1

        while start <= end:
            mid = (start + end) / 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                pivot = mid
                break

        if pivot == -1:
            return [-1, -1]
        else:
            lower = upper = pivot
            last = length - 1

            while upper < last and nums[upper] == nums[upper + 1]:
                upper += 1

            while lower > 0 and nums[lower] == nums[lower - 1]:
                lower -= 1

            return [lower, upper]

sol = Solution()
nums = [5, 7, 7, 8, 8, 10]
print(sol.searchRange(nums, 8))
