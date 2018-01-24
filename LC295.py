from heapq import heappush, heappushpop

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            return float(self.max_heap[0] - self.min_heap[0]) / 2
        else:
            return self.max_heap[0]


class MedianFinder2:
    """
    My own implementation of heaps
    """
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.max_comp = lambda x, y: x > y
        self.min_comp = lambda x, y: x < y

    def heapify(self, heap, comp):
        for parent in range(len(heap) / 2 - 1, -1, -1):
            left = parent * 2 + 1
            right = left + 1

            if right < len(heap) and comp(heap[right], heap[left]) and comp(heap[right], heap[parent]):
                heap[parent], heap[right] = heap[right], heap[parent]
            elif comp(heap[left], heap[parent]):
                heap[parent], heap[left] = heap[left], heap[parent]

    def addNum(self, num):
        if len(self.max_heap) == len(self.min_heap):
            self.min_heap.append(num)
            self.heapify(self.min_heap, self.min_comp)
            self.max_heap.append(self.min_heap.pop(0))
            self.heapify(self.min_heap, self.min_comp)
            self.heapify(self.max_heap, self.max_comp)
        else:
            self.max_heap.append(num)
            self.heapify(self.max_heap, self.max_comp)
            self.min_heap.append(self.max_heap.pop(0))
            self.heapify(self.max_heap, self.max_comp)
            self.heapify(self.min_heap, self.min_comp)

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return float(self.min_heap[0] + self.max_heap[0]) / 2
        else:
            return self.max_heap[0]


m = MedianFinder()

for num in range(10):
    m.addNum(num)

    if num % 3 == 0:
        print(m.findMedian())
        print("Max: ", m.max_heap)
        print("Min: ", m.min_heap)
