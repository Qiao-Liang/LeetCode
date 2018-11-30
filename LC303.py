class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.accu_sum = [0] * (len(nums) + 1)
        self.idx_bnd = -1

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """        
        if j > self.idx_bnd:
            for idx in xrange(self.idx_bnd, j + 1):
                self.accu_sum[idx + 1] = self.accu_sum[idx] + self.nums[idx]
            
            self.idx_bnd = j
        
        return self.accu_sum[j + 1] - self.accu_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


arr = NumArray([-2, 0, 3, -5, 2, -1])

print arr.sumRange(0, 2)
print arr.sumRange(2, 5)
print arr.sumRange(0, 5)
