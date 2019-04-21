class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = cur = set()

        for n in A:
            cur = {n | c for c in cur} | {n}
            res |= cur

        return len(res)


        # len_A = len(A)
        # memo = [[None] * len_A for _ in range(len_A)]
        # key_set = set([])

        # for idx, num in enumerate(A):
        #     memo[idx][idx] = num
        #     key_set.add(num)

        # for row in range(len_A - 1, -1, -1):
        #     for col in range(row + 1, len_A):
        #         memo[row][col] = memo[row + 1][col] | memo[row][col - 1]
        #         key_set.add(memo[row][col])

        # return len(key_set)


sol = Solution()
# a = [1,1,2]
a = [1,2,4]
# a = [1, 11, 6, 11]
print(sol.subarrayBitwiseORs(a))
        