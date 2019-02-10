from random import shuffle

class Solution:

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.rows = n_rows
        self.cols = n_cols
        self.cands = [n for n in range(self.rows * self.cols)]
        self.idx = None
        self.reset()
        

    def flip(self):
        """
        :rtype: List[int]
        """
        self.idx += 1
        temp = self.cands[self.idx]

        return [temp // self.cols, temp % self.cols]


    def reset(self):
        """
        :rtype: void
        """
        shuffle(self.cands)
        self.idx = -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

count = 0
sol = Solution(3, 3)
while sol.cands:
    count += 1
    print(sol.flip())

print("*" * 90)
print(count)

# ["Solution"
# "flip"
# "flip"
# "reset"
# "flip"]
# [[1
# 2]
# []
# []
# []
# []]
