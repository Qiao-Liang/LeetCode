class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = sorted(candidates)
        self.result = []
        self.idx_bound = len(candidates)
        self.dfs(0, target, [])

        return self.result
    
    def dfs(self, curr_idx, target, path):
        if target < 0:
            return
        elif target > 0:
            for idx in range(curr_idx, self.idx_bound):
                if idx > curr_idx and self.candidates[idx] == self.candidates[idx - 1]:
                    continue

                self.dfs(idx + 1, target - self.candidates[idx], path + [self.candidates[idx]])
        else:
            self.result.append(path)
            return


sol = Solution()
# cand = [10, 1, 2, 7, 6, 1, 5]
# target = 8
cand = [4,1,1,4,4,4,4,2,3,5]
target = 10
print(sol.combinationSum2(cand, target))
