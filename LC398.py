from random import randrange

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dic = {}

        for idx, num in enumerate(nums):
            if num in self.dic:
                self.dic[num].append(idx)
            else:
                self.dic[num] = [idx]
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return self.dic[target][randrange(len(self.dic[target]))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

nums = [1, 2, 3, 3, 3]
sol = Solution(nums)
print(sol.pick(3))
print(sol.pick(3))
