class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return None

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) / 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left

sol = Solution()

print(sol.searchInsert([1, 3, 5, 6], 4))
