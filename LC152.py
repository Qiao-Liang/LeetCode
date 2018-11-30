class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = min_val = 1
        res = nums[0]

        for num in nums:
            if num > 0:
                max_val *= num
                min_val *= num
            elif num < 0:
                last_max = max_val
                max_val = min_val * num
                min_val = last_max * num
            else:
                min_val = 1
                max_val = 0

            res = max(res, max_val)
            max_val = max(max_val, 1)

        return res

    def maxProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        len_nums = len(nums)

        for srt in xrange(len_nums):
            temp = nums[srt]
            res = max(res, temp)

            for end in xrange(srt + 1, len_nums):
                temp = temp * nums[end]
                res = max(res, temp)

        return res


sol = Solution()
# nums = [2, 3, -2, 4]
nums = [-2, 0, -1]
# nums = [0, 2]
print sol.maxProduct(nums)
