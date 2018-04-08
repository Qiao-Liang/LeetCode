class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)

        if nums_sum & 1:
            return False

        cache = {}

        def do_partition(srt_idx, target):
            if (srt_idx, target) in cache:
                return cache[(srt_idx, target)]
            
            if target < 0:
                return
            elif target == 0:
                return True
            
            for idx in xrange(srt_idx, len(nums)):
                if do_partition(idx + 1, target - nums[idx]):
                    return True
            
            cache[(srt_idx, target)] = False
            return False
        
        return do_partition(0, nums_sum / 2)

        # sum_nums = sum(nums)

        # if sum_nums & 1:
        #     return False
            
        # target = sum_nums / 2
        # len_nums = len(nums)
        # cache = {}
        # curr_sum = 0

        # for idx, num in enumerate(nums):
        #     curr_sum += num
        #     temp_target = curr_target = target - curr_sum

        #     for loop in xrange(idx + 1, len_nums):
        #         if (loop, curr_target) in cache:
        #              break

        #         if curr_target > nums[loop]:
        #             curr_target -= nums[loop]
        #         elif curr_target < nums[loop]:
        #             pass
        #         else:
        #             return True

        #     cache[(loop, temp_target)] = False

        # return False
                
            # stack = [0] * (len_nums - idx)
            # stack[0] = (idx, target)
            # stack_top = 0

            # while stack_top > -1:
            #     curr_idx = stack[stack_top][0] + 1
            #     curr_target = stack[stack_top][1] - nums[curr_idx]

            #     if curr_target > 0:
            #         stack_top += 1
            #         stack[stack_top] = (curr_idx, curr_target)
            #     elif curr_target < 0:


        # while stack_top > -1:
        #     curr_target = stack[stack_top][1]
        #     curr_num = nums[nums_idx]

        #     if curr_target > curr_num:
        #         stack_top += 1
        #         stack[stack_top] = (nums[nums_idx], curr_target - curr_num)
        #         nums_idx += 1
        #     elif curr_target < curr_num:
        #         cache[(nums_idx, curr_target)] = False
        #         nums_idx += 1
        #     else:
        #         return True

    def canPartition2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        
        if nums_sum & 1:
            return False

        target = nums_sum / 2
        cache = [False] * (target + 1)
        cache[0] = True

        for num in nums:
            for cand in xrange(target, num - 1, -1):
                # cache[cand] = cache[cand] or cache[cand - num]
                cache[cand] = cache[cand - num]

        return cache[target]    


sol = Solution()
# nums = [1, 5, 11, 5]
# nums = [1, 2, 3, 5]
nums = [28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79]

print sol.canPartition(nums)

# from time import time

# t = time()
# print sol.canPartition(nums)
# print time() - t

# t = time()
# print sol.canPartition2(nums)
# print time() - t
