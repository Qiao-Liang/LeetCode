class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        len_total = len(nums1) + len(nums2)

        while k > 0:
            



sol = Solution()
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
print(sol.maxNumber(nums1, nums2, k))

