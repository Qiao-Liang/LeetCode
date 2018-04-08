class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        len_nums = len(nums)
        cache = [None] * len_nums
        cache[0] = (1, 1)
        max_cache = 1

        for out_idx in xrange(1, len_nums):
            temp_max = 0
            temp_count = 1

            for in_idx in xrange(out_idx):
                if nums[in_idx] < nums[out_idx]:
                    if cache[in_idx][0] > temp_max:
                        temp_max = cache[in_idx][0]
                        temp_count = cache[in_idx][1]
                    elif cache[in_idx][0] == temp_max:
                        temp_count += cache[in_idx][1]

            cache[out_idx] = (temp_max + 1, temp_count)
            max_cache = max(cache[out_idx][0], max_cache)

        res = 0

        for item in cache:
            if item[0] == max_cache:
                res += item[1]

        return res


sol = Solution()
nums = [1,3,5,4,7]
# nums = [2,2,2,2,2]
# nums = [1]
# nums = [1,2,4,3,5,4,7,2]
# nums = [1, 3, 2]
print sol.findNumberOfLIS(nums)
        