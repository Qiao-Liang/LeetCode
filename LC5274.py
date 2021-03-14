class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        return 2 ** (steps - 1) % (10 ** 9 + 7)
