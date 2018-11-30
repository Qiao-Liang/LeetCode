class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        max_num = 0
        max_idx = -1

        for idx, val in enumerate(nums):
            if val / 2 >= max_num:
                max_idx = idx
                max_num = val
            elif max_num / 2 < val:
                max_idx = -1

        return max_idx

        '''
        Version 2
        '''

        # if not nums:
        #     return -1

        # if len(nums) == 1:
        #     return 0

        # max_queue = [(-1, float('-inf')), (-1, float('-inf'))]

        # for idx, val in enumerate(nums):
        #     if val > max_queue[1][1]:
        #         max_queue[0] = max_queue[1] 
        #         max_queue[1] = (idx, val)
        #     elif max_queue[0][1] < val < max_queue[1][1]:
        #         max_queue[0] = (idx, val)

        # return max_queue[1][0] if max_queue[0][1] == 0 or (max_queue[0][1] != 0 and max_queue[1][1] / max_queue[0][1] >= 2) else -1

        '''
        Version 1
        '''
        
        # max_idx = 0
        # max_num = nums[0]
        # len_nums = len(nums)

        # for idx in xrange(len_nums):
        #     if nums[idx] > max_num:
        #         max_num = nums[idx]
        #         max_idx = idx

        # for idx in xrange(len_nums):
        #     if idx != max_idx and nums[idx] != 0 and max_num / nums[idx] < 2:
        #         return -1

        # return max_idx


sol = Solution()
nums = [3, 6, 1, 0]
# nums = [1, 2, 3, 4]
# nums = [1, 0]
print(sol.dominantIndex(nums))
        