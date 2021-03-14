class Solution:
    def circularPermutation(self, n: int, start: int):
        return [start ^ i ^ i >> 1 for i in range(1 << n)]

        # res = []

        # for i in range(1 << n):
        #     res.append(i ^ i >> 1)

        # idx = res.index(start)
        # return res[idx:] + res[:idx]
