class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = sorted(candidates)
        self.result = []
        self.last_idx = len(candidates)
        self.dfs(0, target, [])

        return self.result
    
    def dfs(self, curr_idx, target, path):
        if target < 0:
            return
        elif target > 0:
            for idx in range(curr_idx, self.last_idx):
                self.dfs(idx, target - self.candidates[idx], path + [self.candidates[idx]])
        else:
            self.result.append(path)
            return


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
