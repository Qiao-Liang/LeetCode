class Solution:
    def maxSumDivThree(self, nums) -> int:
        nums.sort()
        len_nums = len(nums)
        sm = sum(nums)
        r = sm % 3

        if r == 0:
            return sm

        def check_sum(i, t, s):
            if i >= len_nums or nums[i] > s:
                return False
            else:
                if t + nums[i] == s:
                    return True
                else:
                    return check_sum(i + 1, t, s) or check_sum(i + 1, t + nums[i], s)

        while True:
            if check_sum(0, 0, r):
                break
            else:
                r += 3
        
        return sm - r


sol = Solution()
# p = [3,6,5,1,8]
# p = [1,2,3,4,4]
# p = [2,6,2,2,7]
# p = [4,1,5,3,1]
# p = [2,3,36,8,32,38,3,30,13,40]
p = [3,1,2]
print(sol.maxSumDivThree(p))
