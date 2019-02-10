from random import sample

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set([])
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nums:
            return False
        else:
            self.nums.add(val)
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nums:
            self.nums.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return sample(self.nums, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.insert(2)
param_3 = obj.insert(3)

for idx in range(6):
    print(obj.getRandom())