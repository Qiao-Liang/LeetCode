"""
Path Sum II
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    counter = 0
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return self.pathSumDFS(root, sum, [], [])
        
    def pathSumDFS(self, root, sum, path, result):
        self.counter += 1
        print("Counter: ", self.counter)
        if root:
            path.append(root.val)
            sum -= root.val
            
            print("Path: ", path)
            
            if not root.left and not root.right and sum == 0:
                print("Leaf")
                result.append(path[:])
            
            if root.left:
                print("Left")
                self.pathSumDFS(root.left, sum, path, result)
                path.pop()
                print("Path: ", path, " @ counter: ", self.counter)
            if root.right:
                print("Right")
                self.pathSumDFS(root.right, sum, path, result)
                path.pop()
                print("Path: ", path, " @ counter: ", self.counter)
        # else:
        #     print("Else")
        #     return []
        
        print("Result: ", result, " @ counter ", self.counter)
        return result
        