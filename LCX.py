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

        # left = 0
        # right = len(nums) - 1

        # while left + 1 < right:
        #     mid = (left + right) // 2

        #     if nums[mid] > target:
        #         right = mid
        #     elif nums[mid] < target:
        #         left = mid
        #     else:
        #         while nums[left] != target:
        #             left += 1

        #         while nums[right] != target:
        #             right -= 1

        #         return [left, right]

        # return [-1, -1]


sol = Solution()
# nums = [5,7,7,8,8,8,8,8,10]
nums = [2, 2]
target = 3
# nums = [1, 1]
# target = 1
print(sol.searchRange(nums, target))
        