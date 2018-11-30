from random import shuffle

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.points = []

        for rect in rects:
            width_start = rect[0]
            height_start = rect[1]

            for width in xrange(abs(rect[0] - rect[2]) + 1):
                for height in xrange(abs(rect[1] - rect[3]) + 1):
                    self.points.append([width_start + width, height_start + height])

        shuffle(self.points)
            
    def pick(self):
        """
        :rtype: List[int]
        """
        if len(self.points) > 0:
            return self.points.pop()
        else:
            return None


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()


rects = [[1, 1, 5, 5]]
sol = Solution(rects)
print sol.pick()
print sol.pick()
print sol.pick()
