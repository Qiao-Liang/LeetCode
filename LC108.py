# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) / 2
        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid + 1:])

        return head

    def sortedArrayToBST2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def recurse(l_srt, l_end, r_srt, r_end, head):
            if l_srt == l_end:
                head.left = TreeNode(nums[l_srt])
            elif l_srt > l_end:
                pass
            else:
                mid = (l_srt + l_end) / 2
                head.left = TreeNode(nums[mid])
                recurse(l_srt, mid - 1, mid + 1, l_end, head.left)

            if r_srt == r_end:
                head.right = TreeNode(nums[r_srt])
            elif r_srt > r_end:
                pass
            else:
                mid = (r_srt + r_end) / 2
                head.right = TreeNode(nums[mid])
                recurse(r_srt, mid - 1, mid + 1, r_end, head.right)

        last_idx = len(nums) - 1
        mid = last_idx / 2
        head = TreeNode(nums[mid])

        recurse(0, mid - 1, mid + 1, last_idx, head)

        return head


sol = Solution()
nums = [1, 3, 5, 6, 9, 10, 11, 12]
head = sol.sortedArrayToBST(nums)

print head
