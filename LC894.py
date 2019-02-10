# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 0:
            return None
        elif N == 1:
            return TreeNode(0)
        else:
            def copy_tree(root):
                if root:
                    new_root = TreeNode(0)
                    new_root.left = copy_tree(root.left)
                    new_root.right = copy_tree(root.right)

                    return new_root
                else:
                    return None

            def add_child(root):
                nonlocal count, target_count

                if not root.left and not root.right:
                    count += 1

                    if count == target_count:
                        root.left = TreeNode(0)
                        root.right = TreeNode(0)
                else:
                    if root.left:
                        add_child(root.left)
                    
                    if root.right:
                        add_child(root.right)

            roots = [TreeNode(0)]
            N -= 1
            possibility = 0

            while N > 0:
                possibility += 1
                temp_roots = []

                for root in roots:
                    for poss in range(possibility):
                        temp_root = copy_tree(root)
                        count = 0
                        target_count = poss + 1
                        add_child(temp_root)
                        temp_roots.append(temp_root)

                roots = temp_roots
                N -= 2

            return roots


sol = Solution()
res = sol.allPossibleFBT(7)
print(res)
        