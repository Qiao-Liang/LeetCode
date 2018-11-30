# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        if root.left:
            root.left.next = root.right
            root.right.next = root.next.left if root.next else None

        self.connect(root.left)
        self.connect(root.right)

        # def recurse(left, right):
        #     if left and right:
        #         left.next = right
                
        #         if left.right and right.left:
        #             left.right.next = right.left

        #         recurse(left.left, left.right)
        #         recurse(right.left, right.right)
        
        # recurse(root.left, root.right)

        # return root


n1 = TreeLinkNode(1)
n2 = TreeLinkNode(2)
n3 = TreeLinkNode(3)
n4 = TreeLinkNode(4)
n5 = TreeLinkNode(5)
n6 = TreeLinkNode(6)
n7 = TreeLinkNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

sol = Solution()
sol.connect(n1)
print n1
