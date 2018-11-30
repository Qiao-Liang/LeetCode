class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        idx = 0
        res = 0
        len_nums = len(nums)

        while idx < len_nums:
            res += nums[idx]
            idx += 2

        return res


sol = Solution()
nums = [1,4,3,2]
print(sol.arrayPairSum(nums))
        