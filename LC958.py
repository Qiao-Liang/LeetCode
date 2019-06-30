# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        node_list = [(root, 1)]
        loop_idx = 0

        while loop_idx < len(node_list):
            node, idx = node_list[loop_idx]
            loop_idx += 1

            if node:
                node_list.append((node.left, idx << 1))
                node_list.append((node.right, (idx << 1) + 1))
        
        return node_list[-1][1] == len(node_list)

        # queue = [root]
        # level_count = 1
        
        # while queue:
        #     temp_queue = []
            
        #     for node in queue:
        #         if not node:
        #             return False
                
        #         temp_queue.append(node.left)
        #         temp_queue.append(node.right)

        #     while temp_queue and not temp_queue[-1]:
        #         temp_queue.pop()

        #     if temp_queue and len(queue) != level_count:
        #         return False

        #     level_count <<= 1
        #     queue = temp_queue
        
        # return True


sol = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6

print(sol.isCompleteTree(n1))
