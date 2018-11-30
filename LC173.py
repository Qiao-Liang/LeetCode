# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left 

        # self.min_nodes = []

        # if root:
        #     stack = [root]

        #     while True:
        #         temp = stack.pop()
        #         self.min_nodes.append(temp)

        #         if not temp.left and not temp.right:
        #             break

        #         if temp.right:
        #             stack.append(temp.right)
                
        #         if temp.left:
        #             stack.append(temp.left)             


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

        # return self.min_nodes and any([node is not None for node in self.min_nodes])
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            min_node = self.stack.pop()
            res = min_node.val

            if min_node.right:
                curr = min_node.right

                while curr:
                    self.stack.append(curr)
                    curr = curr.left
            
            return res
        else:
            return None


        # if self.hasNext():
        #     min_val, min_idx = min([(node.val, idx) for idx, node in enumerate(self.min_nodes) if node])
        #     self.min_nodes[min_idx] = None

        #     for idx in xrange(len(self.min_nodes) - 1):
        #         if self.min_nodes[idx] and not self.min_nodes[idx + 1]:
        #             self.min_nodes[idx + 1] = self.min_nodes[idx].left if self.min_nodes[idx].left and self.min_nodes[idx].left.val != min_val else self.min_nodes[idx].right

        #     return min_val
        # else:
        #     return None
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


n3 = TreeNode(3)
n2 = TreeNode(2)
n1 = TreeNode(1)
n4 = TreeNode(4)
n5 = TreeNode(5)
n0 = TreeNode(0)
n6 = TreeNode(6)

n3.left = n1
n3.right = n5
n1.left = n0
# n1.right = n2
# n5.left = n4
n5.right = n6

itr = BSTIterator(n3)

while itr.hasNext():
    print itr.next()
