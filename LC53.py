class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        result = nums[0]
        accum = 0
        for num in nums:
            if accum < 0:
                accum = num
            else:
                accum += num

            if accum > result:
                result = accum
        
        return result

    def maxSubArray_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums= len(nums)
        result = nums[0]
        accum = [nums[0]]

        for num in nums[1:]:
            accum.append(accum[-1] + num)

        for left in range(len_nums):
            result = max(result, accum[left])
            for right in range(left + 1, len_nums):
                result = max(result, accum[right] - accum[left])

        return result


sol = Solution()
# m = [-57,9,-72,-72,-62,45,-97,24,-39,35,-82,-4,-63,1,-93,42,44,1,-75,-25]
m = [-2,1,-3,4,-1,2,1,-5,4]
# m = [-1, -2, -3, -4, -5]

print(sol.maxSubArray(m))
