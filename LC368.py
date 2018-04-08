class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums = sorted(nums)
        len_nums = len(nums)
        cache = [None] * len_nums
        cache[0] = [nums[0]]
        res = [nums[0]]

        for out_idx in xrange(1, len_nums):
            temp_max = []
            curr_num = nums[out_idx]

            for in_idx in xrange(out_idx):
                if curr_num % cache[in_idx][-1] == 0 and len(cache[in_idx]) > len(temp_max):
                    temp_max = cache[in_idx]

            cache[out_idx] = temp_max[:] + [curr_num]

            if len(cache[out_idx]) > len(res):
                res = cache[out_idx]

        return res

    # def largestDivisibleSubset2(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     if not nums:
    #         return []

    #     nums = sorted(nums, reverse=True)
    #     caches = [[nums[0]]]

    #     for num in nums[1:]:
    #         temp = []
    #         for cache in caches:
    #             if cache[-1] % num == 0:
    #                 temp.append(cache[:] + [num])

    #         caches.extend(temp)
    #         caches.append([num])

    #     max_set = []

    #     for temp in caches:
    #         if len(temp) > len(max_set):
    #             max_set= temp
            
    #     return max_set[::-1]


sol = Solution()
# nums = [1]
# nums = [1,2,3,4,6,8,12,24,39]
# nums = [4,8,10,240]
# nums = [1, 2, 4, 8, 16]
nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824]

print sol.largestDivisibleSubset(nums)
