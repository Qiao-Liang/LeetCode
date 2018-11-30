class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}

        for num in nums[1:]:
            temp = {}
            for key, val in dic.items():
                temp[key + num] = temp.get(key + num, 0) + val
                temp[key - num] = temp.get(key - num, 0) + val
            dic = temp
        
        return dic.get(S, 0)

        # if not nums:
        #     return 0

        # self.res = 0

        # def dfs(idx, nums, temp_sum, S):
        #     if idx == len(nums) - 1:
        #         if temp_sum + nums[-1] == S:
        #             self.res += 1

        #         if temp_sum - nums[-1] == S:
        #             self.res += 1
                
        #         return

        #     dfs(idx + 1, nums, temp_sum + nums[idx], S)
        #     dfs(idx + 1, nums, temp_sum - nums[idx], S)

        # dfs(0, nums, 0, S)

        # return self.res


sol = Solution()
nums = [1, 1, 1, 1, 1]
S = 3
# nums = [1, 0]
# S = 1

print(sol.findTargetSumWays(nums, S))
