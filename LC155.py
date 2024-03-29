class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if self.min_stack and self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()