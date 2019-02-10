class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        
        length = len(nums)

        if length & 1 == 0:  # Player A always wins when the length of nums is even
            return True
        
        dp = nums[:]

        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        
        return dp[-1] >= 0


sol = Solution()
nums = [1, 5, 233, 7, 3]
result = sol.PredictTheWinner(nums)
print(result)
