class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        last = len(nums) - 1
        end = last - 1

        for idx in range(0, end):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            first = nums[idx]
            target = -first

            left = idx + 1
            right = last

            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    result.append([first, nums[left], nums[right]])

                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    right -= 1
                    left += 1

        return result


sol = Solution()
nums = [-2, 0, 0, 2, 2]
print(sol.threeSum(nums))
