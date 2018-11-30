# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        curr = root
        parent = None
        which_child = ''

        while curr:
            if key > curr.val:
                parent = curr
                curr = curr.right
                which_child = 'right'
            elif key < curr.val:
                parent = curr
                curr = curr.left
                which_child = 'left'
            else:
                break

        if curr:
            if not curr.left and not curr.right:
                if parent:
                    setattr(parent, which_child, None)
                else:
                    return None
            elif not curr.left or not curr.right:
                if parent:
                    setattr(parent, which_child, curr.left or curr.right)
                else:
                    return curr.left or curr.right
            else:
                temp_child = curr.right
                temp_parent = curr
                which_child = 'right'

                while temp_child.left:
                    temp_parent = temp_child
                    temp_child = temp_child.left
                    which_child = 'left'

                curr.val, temp_child.val = temp_child.val, curr.val
                setattr(temp_parent, which_child, temp_child.right)

        return root

        # parent = None
        # which_child = ''
        # node = root

        # while node:
        #     if node.val < key:
        #         parent = node
        #         node = node.right
        #         which_child = 'right'
        #     elif node.val > key:
        #         parent = node
        #         node = node.left
        #         which_child = 'left'
        #     else:
        #         break

        # if node:
        #     if not node.left and not node.right:
        #         if parent:
        #             parent[which_child] = None
        #     elif node.left and not node.right:
        #         if parent:
        #             parent[which_child] = node.left
        #     elif not node.left and node.right:
        #         if parent:
        #             parent[which_child] = node.right
        #     else:
        #         temp_node = node.right

        #         while temp_node.left:
        #             temp_node = temp_node.left

        #         temp_node.left = node.left
        #         if parent:
        #             parent.left = temp_node

        # return root


sol = Solution()
temp_nodes = [5,3,6,2,4,None,7]
nodes = [TreeNode(val) if val else None for val in temp_nodes]
for idx in range(len(nodes)):
    if nodes[idx] and idx * 2 + 1 < len(nodes):
        nodes[idx].left = nodes[idx * 2 + 1]
    
    if nodes[idx] and idx * 2 + 2 < len(nodes):
        nodes[idx].right = nodes[idx * 2 + 2]

# new_nodes = sol.deleteNode(nodes[0], 0)
new_nodes = sol.deleteNode(nodes[0], 3)

print(new_nodes)
