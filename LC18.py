class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        # left = 0
        # right = len(nums) - 1
        # res = []

        # while right > left:
        #     temp_sum = nums[left] + nums[right]

        #     if temp_sum > 0:
        #         right -= 1
        #     elif temp_sum < 0:
        #         left += 1
        #     else:
        #         temp = [nums[left], nums[right]]

        #         temp_left = left + 1
        #         temp_right = right - 1

        #         while temp_left < temp_right:
        #             temp_sum2 = nums[temp_left] + nums[temp_right]

        #             if temp_sum2 > 0:
        #                 right -= 1
                    

        # self.res = []

        # def recurse(temp_nums, curr_idx, nums, target):
        #     temp_nums.append(nums[curr_idx])

        #     if len(temp_nums) == 4:
        #         if sum(temp_nums) == target:
        #             sorted_nums = sorted(temp_nums)

        #             if sorted_nums not in self.res:
        #                 self.res.append(sorted_nums)

        #         return

        #     for idx in xrange(curr_idx + 1, len(nums)):
        #         recurse(temp_nums, idx, nums, target)
        #         temp_nums.pop()

        # for idx in xrange(0, len(nums)):
        #     recurse([], idx, nums, target)

        # return self.res


sol = Solution()
# s = [-3,-1,0,2,4,5]
# s = [1, 0, -1, 0, -2, 2]
# s = [-3,-2,-1,0,0,1,2,3]
# s = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
s = [-5,5,4,-3,0,0,4,-2]
print(sol.fourSum(s, 4))
