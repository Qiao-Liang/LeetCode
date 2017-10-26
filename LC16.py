class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        maximum = abs(result - target)
        last = len(nums) - 1
        end = last - 1

        for idx in range(0, end):
            if idx > 2 and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = last

            while left < right:
                temp = nums[idx] + nums[left] + nums[right]

                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    return target

                abs_dist = abs(temp - target)
                if abs_dist < maximum:
                    maximum = abs_dist
                    result = temp

        return result


from time import time
sol = Solution()
nums = [1] * 100 + [0]
t = time()
result = sol.threeSumClosest(nums, 100)
print(time() - t)
print(result)
