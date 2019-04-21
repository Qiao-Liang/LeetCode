class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):
            extra = len(nums) - k

            if extra == 0:
                return nums

            stack = []

            for num in nums:
                while extra and stack and stack[-1] < num:
                    stack.pop()
                    extra -= 1

                stack.append(num)

            return stack[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in range(k)]

        return max(merge(prep(nums1, i), prep(nums2, k - i)) for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2))


sol = Solution()
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
print(sol.maxNumber(nums1, nums2, k))

