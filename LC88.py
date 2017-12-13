class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums2:
            for m_idx in range(m):
                if nums1[m_idx] > nums2[0]:
                    nums1[m_idx], nums2[0] = nums2[0], nums1[m_idx]

                    for n_idx in range(n - 1):
                        if nums2[n_idx] > nums2[n_idx + 1]:
                            nums2[n_idx], nums2[n_idx + 1] = nums2[n_idx + 1], nums2[n_idx]
                        else:
                            break

            nums1 = nums1[:m] + nums2[:n]
        
        print(nums1)


# m = [1, 3, 4, 6, 9]
m = [0]
# n = [2, 5, 7, 8]
n = [1]
sol = Solution()
sol.merge(m, 0, n, 1)
