class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        self.memo = {}

        return self.dfs([num for num in range(1, maxChoosableInteger + 1)], 0, desiredTotal)

    def dfs(self, cands, curr_sum, target):
        if len(cands) == 0:
            return False

        key = tuple(cands)

        if key in self.memo:
            return self.memo[key]
        else:
            self.memo[key] = False

            if max(cands) + curr_sum >= target:
                self.memo[key] = True
            else:
                for cand in cands:
                    if not self.dfs([num for num in cands if num != cand], curr_sum + cand, target):
                        self.memo[key] = True
                        break
            
            return self.memo[key]


sol = Solution()
maxChoosableInteger = 10
desiredTotal = 40

print(sol.canIWin(maxChoosableInteger, desiredTotal))
