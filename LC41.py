class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        max_num = len(nums)
        
        if max_num == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1

        for idx, val in enumerate(nums):
            if val < 0 or val >= max_num:
                nums[idx] = 0
        
        for num in nums:
            nums[num % max_num] += max_num

        idx = 1

        while idx < max_num:
            if nums[idx] < max_num:
                return idx
            
            idx += 1

        return max_num + 1

        # nums.append(0)
        # max_num = len(nums)

        # for idx, val in enumerate(nums):
        #     if val < 0 or val >= max_num:
        #         nums[idx] = 0
        
        # for num in nums:
        #     nums[num % max_num] += max_num

        # idx = 1
        # while idx < max_num:
        #     if nums[idx] < max_num:
        #         return idx
            
        #     idx += 1

        # return max_num

    def firstMissingPositive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_sum = 0
        pos_cnt = 0
        pos_max = 0

        for num in nums:
            if num > 0:
                pos_sum += num
                pos_cnt += 1
                pos_max = max(pos_max, num)

        if pos_cnt == pos_max:
            return pos_max + 1
        else:
            while pos_max - pos_cnt > 1:
                pos_max = ((1 + pos_max) * pos_max / 2 - pos_sum) / (pos_max - pos_cnt)
                pos_cnt = 0
                pos_sum = 0

                for num in nums:
                    if 0 < num < pos_max:
                        pos_sum += num
                        pos_cnt += 1

            return (1 + pos_max) * pos_max / 2 - pos_sum


sol = Solution()
# nums = [6, 3, 4, -1, 1]
# nums = [1, 1]
nums = [1, 2, 0]
# nums = [-1]
# nums = [2, 1]
# nums = [0, 3]
print(sol.firstMissingPositive(nums))
