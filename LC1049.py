class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        memo = {0}

        for stone in stones:
            memo = {stone + temp for temp in memo} | {stone - temp for temp in memo}
        
        return min(abs(temp) for temp in memo)


        # def recurse(stones):
        #     len_stones = len(stones)

        #     if len_stones == 1:
        #         self.res = min(self.res, stones[0])
        #         return
        #     elif len_stones == 0:
        #         self.res = 0
        #         return

        #     if self.res > 0:
        #         for idx in range(1, len_stones):
        #             stone1, stone2 = stones[idx - 1], stones[idx]
        #             temp_stones = stones[:]
        #             temp_stones.remove(stone1)
        #             temp_stones.remove(stone2)

        #             if stone1 != stone2:
        #                 temp_stones.append(stone2 - stone1)
        #                 temp_stones.sort()

        #             recurse(temp_stones)
        
        # recurse(stones)
        # return self.res


        # stones.sort()

        # while len(stones) > 1:
        #     max_idx = max_diff = 0

        #     for idx in range(1, len(stones)):
        #         temp_diff = stones[idx] - stones[idx - 1]

        #         if temp_diff > max_diff:
        #             max_diff = temp_diff
        #             max_idx = idx
                
        #     stone1, stone2 = stones[max_idx - 1], stones[max_idx]
        #     stones.remove(stone1)
        #     stones.remove(stone2)

        #     if stone1 != stone2:
        #         stones.append(stone2 - stone1)
        #         stones.sort()
                
        # return stones[0] if stones else 0


sol = Solution()
# s = [2,7,4,1,8,1]
s = [1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98]
# s = [1,2,4,8,16,32,64,12,25,51]
# s = [1, 1, 1, 1, 1]
print(sorted(s))
print(sol.lastStoneWeightII(s))
