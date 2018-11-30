class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        len_nums = len(nums)
        res = 0
        slow = fast = 0

        while slow < len_nums:
            if nums[slow] == 1:
                fast = slow

                while fast < len_nums and nums[fast] == 1:
                    fast += 1

                res = max(res, fast - slow)
                slow = fast
            else:
                slow += 1

        return res


sol = Solution()
nums = [1,1,0,1,1,1]
# nums = [0, 0, 0, 0, 0]
print(sol.findMaxConsecutiveOnes(nums))
