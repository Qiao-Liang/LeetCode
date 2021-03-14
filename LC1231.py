class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        l, r = 1, sum(sweetness) // (K + 1)

        while l < r:
            m = (l + r + 1) // 2
            cur = cuts = 0

            for s in sweetness:
                cur += s

                if cur >= m:
                    cuts += 1
                    cur = 0

            if cuts > K:
                l = m
            else:
                r = m - 1

        return r


sol = Solution()
p = [[1,2,3,4,5,6,7,8,9], 5]
print(sol.maximizeSweetness(*p))
