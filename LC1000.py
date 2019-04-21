class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        length = len(stones)
        INF = float('inf')
        pre_sum = [0] * (length + 1)
        pre_sum[0] = stones[0]

        for idx in range(length):
            pre_sum[idx + 1] = pre_sum[idx] + stones[idx]

        from functools import lru_cache

        @lru_cache(None)
        def dp(start, end, piles):
            if (end - start + 1 - piles) % (K - 1):
                return INF
            
            if start == end:
                return 0 if piles == 1 else INF
            
            if piles == 1:
                return dp(start, end, K) + pre_sum[end + 1] - pre_sum[start]

            return min(dp(start, temp, 1) + dp(temp + 1, end, piles - 1) for temp in range(start, end, K - 1))

        res = dp(0, length - 1, 1)
        return res if res < INF else -1

        # temp_length = length = len(stones)

        # while temp_length > K:
        #     temp_length -= K - 1

        # if temp_length != K:
        #     return -1

        # memo = [[None] * length for _ in range(length)]

        # for idx in range(length):
        #     memo[idx][idx] = stones[idx]

        # for start in range(length):
        #     for end in range(start + 1, length):
        #         memo[start][end] = memo[start][end - 1] + stones[end]
        
        # return -1

        # for idx in range(length):
        #     memo[idx][idx] = stones[idx]

        #     if idx + K - 1 < length:
        #         memo[idx][idx + K - 1] = sum(stones[idx: idx + K])

        
        # def recurse(start, end):
        #     if memo[start][end] is not None:
        #         return memo[start][end]

        #     if end - start + 1 <= K:
        #         return sum(stones[start: end + 1])

        #     res = float('inf')

        #     for curr in range(start, end + 1):
        #         temp = 0
        #         temp += recurse(start, curr)
        #         temp += sum(stones[curr: curr + K])
        #         temp += recurse(curr + K, end)
        #         res = min(res, temp * 2)

        #     memo[start][end] = res
        #     return res

        # recurse(0, length - 1)
        # return memo[0][length - 1]


sol = Solution()
stones = [3,2,4,1]
K = 2
# stones = [3,5,1,2,6]
# K = 3
print(sol.mergeStones(stones, K))
