class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.list = A
        self.idx = 0
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.idx < len(self.list) and n > self.list[self.idx]:
            n -= self.list[self.idx]
            self.list[self.idx] = 0
            self.idx += 2

        if self.idx < len(self.list):
            self.list[self.idx] -= n

            return self.list[self.idx + 1]
        else:
            return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

A = [3,8,0,9,2,5]
obj = RLEIterator(A)
print(obj.next(2))
print(obj.next(1))
print(obj.next(1))
print(obj.next(2))
