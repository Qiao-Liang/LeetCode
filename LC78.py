class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()

        for num in nums:
            result.extend([elem + [num] for elem in result])

        return result

    def subsets_dfs(self, nums):
        self.result = []
        self.last_idx = len(nums)
        self.nums = nums
        self.nums.sort()

        self.dfs(0, [])
        return self.result

    def dfs(self, curr_idx, path):
        self.result.append(path)
        for idx in range(curr_idx, self.last_idx):
            self.dfs(idx + 1, path + [self.nums[idx]])


sol = Solution()
# print(sol.subsets_dfs([1, 2, 3]))
print(sol.subsets([1, 2, 3]))
