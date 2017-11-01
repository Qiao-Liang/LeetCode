class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        temp = 1

        for num in nums:
            result.append(temp)
            temp *= num

        temp = 1
        last_idx = len(nums) - 1

        for idx in range(last_idx, -1, -1):
            result[idx] *= temp
            temp *= nums[idx]

        return result

sol = Solution()
nums = [1, 2, 3, 4]
print(sol.productExceptSelf(nums))
