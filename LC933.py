class RecentCounter(object):

    def __init__(self):
        self.history = []
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.history.append(t)

        while t - self.history[0] > 3000:
            self.history.pop(0)

        return len(self.history)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)