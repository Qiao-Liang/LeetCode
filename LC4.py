class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        med = total_len // 2
        is_odd = total_len & 1

        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
            
            med -= 1

            if med == 0:
                if nums1[0] < nums2[0]:
                    temp = nums1.pop(0)
                else:
                    temp = nums2.pop(0)

                if is_odd:
                    return temp
                else:
                    return (temp + min(nums1))