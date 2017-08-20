class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0

        nums = sorted(nums)
        len_nums = len(nums)
        count = 0

        for i in range(2, len_nums):
            first, second = 0, i - 1

            while first < second:
                if nums[first] + nums[second] > nums[i]:
                    count += (second - first)
                    second -= 1
                else:
                    first += 1
        
        return count


sol = Solution()
a = [2, 2, 3, 4]
print(sol.triangleNumber(None))