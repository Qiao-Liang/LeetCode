"""
Find Median from Data Stream
"""

class MedianFinder:
    tupNum = []

    def __init__(self):
      self.tupNum = [float('-Inf'), float('Inf')]

    def addNum(self, num):
        for idx in range(0, len(self.tupNum) - 1):
            if num > self.tupNum[idx] and num <= self.tupNum[idx + 1]:
                self.tupNum.insert(idx + 1, num)

    def findMedian(self):
      intLen = len(self.tupNum)

      if intLen % 2 == 0:
          return ((float(self.tupNum[intLen/2 - 1]) + float(self.tupNum[intLen/2]))/2)
      else:
        if intLen == 1:
          return (float(self.tupNum[0]))
        else:
          return (float(self.tupNum[(intLen - 1)/2]))