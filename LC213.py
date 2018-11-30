class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        len_nums = len(nums)

        if len_nums < 3:
            return max(nums)

        res = 0

        def get_prev_idx(prev_idx):
            return prev_idx if prev_idx >= 0 else len_nums + prev_idx

        for idx in xrange(len_nums):
            memo = [0] * len_nums
            memo[idx] = nums[idx]
            memo[(idx + 1) % len_nums] = max(nums[(idx + 1) % len_nums], nums[idx])
            curr = (idx + 2) % len_nums
            counter = len_nums - 2

            while counter > 0:
                if (curr + 1) % len_nums != idx:
                    memo[curr] = max(memo[get_prev_idx(curr - 1)], memo[get_prev_idx(curr - 2)] + nums[curr])
                else:
                    memo[curr] = memo[get_prev_idx(curr - 1)]

                curr = (curr + 1) % len_nums
                counter -= 1

            res = max(res, memo[-1])

        return res


sol = Solution()
# nums = [1, 2, 3, 1]
# nums = [2, 3, 2]
nums = [1, 7, 9, 2]
print sol.rob(nums)
