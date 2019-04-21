class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        
        if not nums:
            return res
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[right] != target:
            return res

        res[0] = left
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        res[1] = right - 1

        return res

        # length = len(nums)
        # start = 0
        # end = length - 1
        # pivot = -1

        # while start <= end:
        #     mid = (start + end) / 2

        #     if nums[mid] > target:
        #         end = mid - 1
        #     elif nums[mid] < target:
        #         start = mid + 1
        #     else:
        #         pivot = mid
        #         break

        # if pivot == -1:
        #     return [-1, -1]
        # else:
        #     lower = upper = pivot
        #     last = length - 1

        #     while upper < last and nums[upper] == nums[upper + 1]:
        #         upper += 1

        #     while lower > 0 and nums[lower] == nums[lower - 1]:
        #         lower -= 1

        #     return [lower, upper]


sol = Solution()
nums = [5, 7, 7, 8, 8, 10]
print(sol.searchRange(nums, 8))
