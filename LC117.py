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
        level_head = temp_head = TreeLinkNode(-1)

        while root:            
            if root.left:
                temp_head.next = root.left
                temp_head = temp_head.next

            if root.right:
                temp_head.next = root.right
                temp_head = temp_head.next

            temp_head.next = None

            if root.next:
                root = root.next
            else:
                root = level_head.next
                temp_head = level_head
        
        # if not root:
        #     return

        # nodes = []

        # if root.left:
        #     nodes.append(root.left)
        # if root.right:
        #     nodes.append(root.right)
        # if root.next:
        #     if root.next.left:
        #         nodes.append(root.next.left)
        #     if root.next.right:
        #         nodes.append(root.next.right)
        
        # for idx in xrange(len(nodes) - 1):
        #     nodes[idx].next = nodes[idx + 1]

        # self.connect(root.left)
        # self.connect(root.right)


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
# n3.left = n6
n3.right = n7

sol = Solution()
sol.connect(n1)
print n1
