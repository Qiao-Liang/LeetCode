class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        idx = [i for i, n in enumerate(nums) if n & 1]
        len_nums = len(nums)
        len_idx = len(idx)
        l = 0
        r = k - 1
        res = 0

        while r < len_idx:
            res += ((idx[l] - idx[l - 1]) if l > 0 else idx[l] + 1) * ((idx[r + 1] - idx[r]) if r + 1 < len_idx else len_nums - idx[r])
            r += 1
            l += 1

        return res

        # len_nums = len(nums)
        # res = 0
        # pre_count = [0] * (len_nums + 1)

        # for i in range(1, len_nums + 1):
        #     pre_count[i] = pre_count[i - 1] + (nums[i - 1] & 1)

        # for l in range(1, len_nums + 1):
        #     for c in range(l):
        #         if pre_count[l] - pre_count[c] == k:
        #             res += 1 

        # return res


sol = Solution()
# p = [[1,1,2,1,1], 3]
p = [[2,2,2,1,2,2,1,2,2,2], 2]
print(sol.numberOfSubarrays(*p))
