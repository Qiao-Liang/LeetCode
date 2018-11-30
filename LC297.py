# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            node = queue.pop(0)

            if not node:
                res.append(None)
                continue
            
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

            # temp_queue = []

            # for node in queue:
            #     if node is None:
            #         temp_queue.append(None)
            #         temp_queue.append(None)
            #     else:
            #         temp_queue.append(node.left)
            #         temp_queue.append(node.right)

            # if any(temp_queue):
            #     res.extend([node.val if node is not None else None for node in temp_queue])
            #     queue = temp_queue
            # else:
            #     queue = None
        
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        len_data = len(data)

        for idx, val in enumerate(data):
            if val is not None:
                data[idx] = TreeNode(val)

        for idx, node in enumerate(data):
            if node is not None:
                left_idx = idx * 2 + 1
                right_idx = idx * 2 + 2

                if left_idx < len_data:
                    node.left = data[left_idx]

                if right_idx < len_data:
                    node.right = data[right_idx]

        return data[0]

            
            # temp = TreeNode(val)
            # left_idx = idx * 2 + 1
            # right_idx = left_idx + 1

            # if left_idx < len_data and data[left_idx]:
            #     temp.left = TreeNode(data[left_idx])
            
            # if right_idx < len_data:
            #     temp.right = TreeNode(data[right_idx])

            # if not root:
            #     root = temp

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


code = Codec()
# arr = [1,2,3,None,None,4,5]
# arr = [-1, 0, 1]
arr = [5,2,3,None,None,2,4,3,1]
head = code.deserialize(arr)

print code.serialize(head)
