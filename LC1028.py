# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        bound = len(S)
        self.idx = 0

        def dfs(level):
            dash_count = 0
            idx_srt = self.idx

            while self.idx < bound and S[self.idx] == '-':
                dash_count += 1
                self.idx += 1
            
            if dash_count == level:
                idx_int = self.idx

                while self.idx < bound and S[self.idx] != '-':
                    self.idx += 1

                node = TreeNode(int(S[idx_int: self.idx]))
                node.left = dfs(level + 1)
                node.right = dfs(level + 1)
                return node
            else:
                self.idx = idx_srt
                return None
        
        return dfs(0)


sol = Solution()
s = "1-2--3--4-5--6--7"
node = sol.recoverFromPreorder(s)
print(node)
