class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        curr = 0

        for num in nums2:
            while curr < m and nums1[curr] <= num:
                curr += 1

            temp_curr = m
            m += 1

            while temp_curr > curr:
                nums1[temp_curr] = nums1[temp_curr - 1]
                temp_curr -= 1
                
            nums1[curr] = num

        print nums1


        # if nums2:
        #     for m_idx in range(m):
        #         if nums1[m_idx] > nums2[0]:
        #             nums1[m_idx], nums2[0] = nums2[0], nums1[m_idx]

        #             for n_idx in range(n - 1):
        #                 if nums2[n_idx] > nums2[n_idx + 1]:
        #                     nums2[n_idx], nums2[n_idx + 1] = nums2[n_idx + 1], nums2[n_idx]
        #                 else:
        #                     break

        #     nums1 = nums1[:m] + nums2[:n]
        
        # print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
