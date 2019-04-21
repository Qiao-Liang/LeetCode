# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)

        queue = [target]
        visited = set([target])

        while K > 0 and queue:
            K -= 1
            temp_queue = []

            for node in queue:
                for neib in graph[node]:
                    if neib not in visited:
                        visited.add(neib)
                        temp_queue.append(neib)
            
            queue = temp_queue

        if K == 0:
            return [node.val for node in queue]
        else:
            return []


        # self.target_node = None
        # self.parent = {}
        # res = []

        # def dfs(node, parent):
        #     if not node:
        #         return

        #     self.parent[node] = parent

        #     if node == target:
        #         self.target_node = node
        #         return
            
        #     dfs(node.left, node)
        #     dfs(node.right, node)
            
        # dfs(root, None)

        # if not self.target_node:
        #     return []

        # temp = K - 1
        # temp_parent = self.parent[self.target_node]

        # if temp == 0 and temp_parent:
        #     res.append(temp_parent.val)

        # while temp > 0 and temp_parent:
        #     temp_sub = K - temp
        #     temp -= 1
        #     queue = [temp_parent]

        #     while temp_sub and queue:
        #         temp_sub -= 1
        #         temp_queue = []

        #         for temp_node in queue:
        #             if temp_node.left:
        #                 temp_queue.append(temp_node.left)
                    
        #             if temp_node.right:
        #                 temp_queue.append(temp_node.right)

        #         queue = temp_queue

        #     if temp_sub == 0 and queue:
        #         res.extend([node.val for node in queue if node != target])

        #     temp_parent = self.parent[temp_parent]

        # queue = [self.target_node]

        # while K > 0 and queue:
        #     K -= 1
        #     temp_queue = []

        #     for temp_node in queue:
        #         if temp_node.left:
        #             temp_queue.append(temp_node.left)

        #         if temp_node.right:
        #             temp_queue.append(temp_node.right)

        #     queue = temp_queue

        # if K == 0 and queue:
        #     res.extend([node.val for node in queue])

        # return res


sol = Solution()
node0 = TreeNode(3)
node1 = TreeNode(5)
node2 = TreeNode(1)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(0)
node6 = TreeNode(8)
node7 = TreeNode(7)
node8 = TreeNode(4)

node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
node4.left = node7
node4.right = node8

print(sol.distanceK(node0, node1, 1))
