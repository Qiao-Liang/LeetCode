from heapq import heapify, heappush, heappop, heapreplace #, nlargest

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapify(self.heap)

        while len(self.heap) > k:
            heappop(self.heap)        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heapreplace(self.heap, val)

        return self.heap[0]

        # heappush(self.heap, val)
        # return nlargest(self.k, self.heap)[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


arr = [4,5,8,2]
kthLargest = KthLargest(3, arr)
kthLargest.add(3)
kthLargest.add(5)
kthLargest.add(10)
kthLargest.add(9)
# kthLargest.add(4)
