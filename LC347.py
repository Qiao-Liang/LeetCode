class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Counter the frequency of each number
        freq_dict = {}
        heap = []
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                heap.append(num)
                freq_dict[num] = 1
        
        # Initiate a max heap
        heap_size = len(heap)
        for i in range(heap_size//2 - 1, -1, -1):
            self.heapify(heap, freq_dict, heap_size, i)
        
        # Do heap sort and stop after k rounds
        for i in range(heap_size - 1, heap_size - k - 1, -1):
            heap[i], heap[0] = heap[0], heap[i]
            self.heapify(heap, freq_dict, i, 0)

        return heap[heap_size - k:][::-1]

    def heapify(self, heap, freq_dict, heap_size, idx):
        max_idx = idx
        lc_idx = 2 * idx + 1
        rc_idx = 2 * idx + 2

        if lc_idx < heap_size and freq_dict[heap[lc_idx]] > freq_dict[heap[idx]]:
            max_idx = lc_idx

        if rc_idx < heap_size and freq_dict[heap[rc_idx]] > freq_dict[heap[max_idx]]:
            max_idx = rc_idx
        
        if max_idx != idx:
            heap[idx], heap[max_idx] = heap[max_idx], heap[idx]
            self.heapify(heap, freq_dict, heap_size, max_idx)
