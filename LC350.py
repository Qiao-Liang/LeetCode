class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = {}
        dic2 = {}
        common = set(nums1) & set(nums2)

        for num1 in nums1:
            if num1 in dic1:
                dic1[num1] += 1
            else:
                dic1[num1] = 1

        for num2 in nums2:
            if num2 in dic2:
                dic2[num2] += 1
            else:
                dic2[num2] = 1

        res = []

        for num in common:
            res.extend([num] * min(dic1[num], dic2[num]))

        return res

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
        #         # idx1 = get_next(nums1, idx1, len_1)
        #         # idx2 = get_next(nums2, idx2, len_2)
        #         idx1 += 1
        #         idx2 += 1

        # return res


sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersect(nums1, nums2))
