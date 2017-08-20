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
            for key, val in dic.iteritems():
                temp[key + num] = temp.get(key + num, 0) + val
                temp[key - num] = temp.get(key - num, 0) + val
            dic = temp
        
        return dic.get(S, 0)

sol = Solution()
nums = [1, 1, 2, 1, 1]
S = 4

print(sol.findTargetSumWays(nums, S))
