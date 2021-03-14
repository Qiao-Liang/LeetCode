class Solution:
    def findMaxLength(self, nums) -> int:
        l = len(nums) + 1
        c0 = [0] * l
        c1 = [0] * l
        res = 0
        
        for i, n in enumerate(nums):
            if n == 0:
                c0[i] = c0[i - 1] + 1
                c1[i] = c1[i - 1]
            else:
                c0[i] = c0[i - 1]
                c1[i] = c1[i - 1] + 1
        
        for s in range(1, l):
            for e in range(s, l):
                if c0[e] - c0[s] == c1[e] - c1[s]:
                    res = max(res, e - s + 1)
        
        return res


sol = Solution()
print(sol.findMaxLength([0, 1, 1]))
