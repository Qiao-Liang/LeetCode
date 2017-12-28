class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)

        if len_nums == 0:
            return None
        elif len_nums == 1:
            return 0
        else:
            if nums[1] < nums[0]:
                return 0

            for idx in range(1, len_nums):
                if nums[idx]  <nums[idx - 1]:
                    return idx - 1

            return len_nums - 1

sol = Solution()
print(sol.findPeakElement([1, 2, 3]))
