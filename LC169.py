class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_nums = {}
        threshold = len(nums) / 2

        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1

            if dict_nums[num] > threshold:
                return num

        return None


sol = Solution()
print(sol.majorityElement([1]))
