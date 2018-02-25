class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            temp_idx = abs(num) - 1
            nums[temp_idx] = -abs(nums[temp_idx])

        return [idx + 1 for idx in xrange(len(nums)) if nums[idx] > 0]

        # if not nums:
        #     return []

        # max_num = len(nums)

        # if sum(nums) == (1 + max_num) * max_num / 2:
        #     return []

        # result = []

        # for num in nums:
        #     nums[num % max_num] += max_num

        # idx = 1
        # while idx < max_num:
        #     if nums[idx] <= max_num:
        #         result.append(idx)

        #     idx += 1

        # if not result:
        #     result.append(max_num)

        # return result


sol = Solution()
nums = [4,3,2,7,8,2,3,1]
# nums = [1, 1]
# nums = [2, 2]
# nums = [1, 2]
# nums = [1, 1, 2, 2]
print(sol.findDisappearedNumbers(nums))
