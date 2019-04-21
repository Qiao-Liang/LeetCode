class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num_set = set(nums)
        dp = [1 if num in num_set else 0 for num in range(target + 1)]
        nums.sort()

        for num1 in range(1, target + 1):
            for num2 in range(1, num1):
                if num2 in num_set:
                    dp[num1] += dp[num1 - num2]

        return dp[-1]


sol = Solution()
nums = [1, 2, 3]
target = 4
# nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# target = 10
# nums = [1,2]
# target = 10
print(sol.combinationSum4(nums, target))
