class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1


sol = Solution()
# nums = [-1,0,3,5,9,12]
# target = 9
# nums = [-1,0,3,5,9,12]
# target = 2
nums = [5]
target = 5
print(sol.search(nums, target))
        