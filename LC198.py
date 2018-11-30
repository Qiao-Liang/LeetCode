class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        len_nums = len(nums)

        if len_nums < 3:
            return max(nums)

        memo = [0] * len_nums
        memo[0] = nums[0]
        memo[1] = max(nums[1], nums[0])

        for idx in xrange(2, len_nums):
            memo[idx] = max(memo[idx - 1], memo[idx - 2] + nums[idx])

        return memo[-1]


sol = Solution()
# nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]
print sol.rob(nums)
