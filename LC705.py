class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [[0] * 1000 for _ in range(1000)]
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hash[key // 1000][key % 1000] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hash[key // 1000][key % 1000] = 0
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.hash[key // 1000][key % 1000] == 1



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


hash = MyHashSet()
hash.add(1)
hash.add(10)
print(hash.contains(1))
hash.remove(1)
print(hash.contains(1))
