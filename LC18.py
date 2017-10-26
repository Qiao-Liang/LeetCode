class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        left = 0
        last = len(nums) - 1
        right = last
        nums.sort()
        result = []

        while right - left > 2:
            if left > 0 and right < last and nums[left] == nums[left - 1] and nums[right] == nums[right + 1]:
                left += 1
                right -= 1
                continue
            
            inner_target = target - nums[left] - nums[right]
            inner_left = left + 1
            inner_right = right - 1
            inner_sum = nums[inner_left] + nums[inner_right]
            found = False

            while inner_left < inner_right:
                if inner_left > left + 1 and inner_right < right - 1 and nums[inner_left] == nums[inner_left - 1] and nums[inner_right] == nums[inner_right + 1]:
                    inner_left += 1
                    inner_right -= 1
                    continue

                inner_sum = nums[inner_left] + nums[inner_right]

                if inner_sum < inner_target:
                    inner_left += 1
                elif inner_sum > inner_target:
                    inner_right -= 1
                else:
                    found = True
                    result.append([nums[left], nums[inner_left], nums[inner_right], nums[right]])

                    inner_left += 1
                    inner_right -= 1
                
            if found:
                left += 1
                right -= 1
            else:
                if nums[right] - nums[right - 1] < nums[left + 1] - nums[left]:
                    right -= 1
                else:
                    left += 1

        return result

sol = Solution()
s = [-3,-1,0,2,4,5]
# s = [1, 0, -1, 0, -2, 2]
print(sol.fourSum(s, 0))
