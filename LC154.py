class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # left, right = 0, len(nums) - 1

        # while left < right:
        #     mid = (left + right) // 2

        #     if nums[mid] < nums[right]:
        #         right = mid
        #     elif nums[mid] > nums[right]:
        #         left = mid + 1

        # return nums[left]


sol = Solution()
nums = [2,2,2,0,1]
print(sol.findMin(nums))
