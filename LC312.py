class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 1)
        nums.append(1)
        len_nums = len(nums)
        dp = [[0] * len_nums for _ in range(len_nums)]

        for l in range(1, len_nums - 1):
            for si in range(1, len_nums - l):
                ei = si + l - 1

                for k in range(si, ei + 1):
                    dp[si][ei] = max(dp[si][ei], dp[si][k - 1] + nums[si - 1] * nums[k] * nums[ei + 1] + dp[k + 1][ei])

        return dp[1][len_nums - 2]

    def maxCoins2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        self.res = 0

        def recurse(temp_sum, bursted):
            if len_nums == len(bursted):
                self.res = max(self.res, temp_sum)
            else:
                set_bursted = set(bursted)

                for i in range(len_nums):
                    if i not in bursted:
                        l = i - 1
                        r = i + 1

                        while l > -1 and l in set_bursted:
                            l -= 1

                        while r < len_nums and r in set_bursted:
                            r += 1

                        bursted.append(i)
                        recurse(temp_sum + nums[i] * (nums[l] if l > -1 else 1) * (nums[r] if r < len_nums else 1), bursted)
                        bursted.pop()

        recurse(0, [])
        return self.res


sol = Solution()
nums = [3,1,5,8]
# nums = [3, 1, 5]
# nums = [35,16,83,87,84,59,48,41,20,54]
print(sol.maxCoins(nums))
