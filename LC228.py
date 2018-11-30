class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        curr = 0
        start = end = nums[0]
        bound = len(nums) - 1
        res = []

        def append(start, end, res):
            if start == end:
                    res.append(str(start))
            else:
                res.append("{}->{}".format(start, end))

        while curr < bound:
            curr += 1
            if nums[curr] - nums[curr - 1] == 1:
                end = nums[curr]
            else:
                append(start, end, res)
                start = end = nums[curr]

        append(start, end, res)

        return res


sol = Solution()
# nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
print sol.summaryRanges(nums)
        