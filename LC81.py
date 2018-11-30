class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0 
        right = len(nums) - 1
        
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1

            mid = (left + right) / 2

            if nums[mid] == target:
                return True
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return False


sol = Solution()
nums = [2,5,6,0,0,1,2]
print sol.search(nums, 1)        
        