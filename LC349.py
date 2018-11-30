class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        Version 3
        '''
        nums1 = set(nums1)
        nums2 = set(nums2)

        return list(nums1 & nums2)

        '''
        Version 2
        '''
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # res = []

        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1

        # for num in nums1:
        #     if num in nums2:
        #         res.append(num)

        # return res

        '''
        Version 1
        '''
        # nums1 = sorted(nums1)
        # nums2 = sorted(nums2)
        # len_1 = len(nums1)
        # len_2 = len(nums2)
        # idx1 = idx2 = 0
        # res = []

        # def get_next(nums, idx, len_nums):
        #     while idx + 1 < len_nums and nums[idx + 1] == nums[idx]:
        #         idx += 1

        #     return idx + 1

        # while idx1 < len_1 and idx2 < len_2:
        #     if nums1[idx1] > nums2[idx2]:
        #         idx2 = get_next(nums2, idx2, len_2)
        #     elif nums1[idx1] < nums2[idx2]:
        #         idx1 = get_next(nums1, idx1, len_1)
        #     else:
        #         res.append(nums1[idx1])
        #         idx1 = get_next(nums1, idx1, len_1)
        #         idx2 = get_next(nums2, idx2, len_2)

        # return res


sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
print(sol.intersection(nums1, nums2))
        