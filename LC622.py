class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [None] * k
        self.head = None
        self.tail = None
        self.length = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.head = 0
                self.tail = 0
            else:
                self.tail += 1
                self.tail %= self.length

            self.queue[self.tail] = value
            return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = None
            self.head += 1
            self.head %= self.length

            if (self.tail + 1) % self.length == self.head:
                self.head = None
                self.tail = None
            
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.queue[self.head]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.queue[self.tail]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.head is None and self.tail is None
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return not self.isEmpty() and (self.tail + 1) % self.length == self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

queue = MyCircularQueue(3)
print(queue.isEmpty())
print(queue.Front())
print(queue.Rear())
print(queue.enQueue(1))
print(queue.queue)
print(queue.enQueue(2))
print(queue.queue)
print(queue.enQueue(3))
print(queue.queue)
print(queue.isFull())
print(queue.Front())
print(queue.Rear())
print(queue.enQueue(4))
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.isEmpty())

