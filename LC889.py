# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def build_subtree(pre_idx, post_idx, len_subtree):
            if len_subtree < 1:
                return None

            root = TreeNode(pre[pre_idx])
            
            if len_subtree == 1:
                return root

            temp_post_idx = dic_post[pre[pre_idx + 1]]
            temp_len_subtree = temp_post_idx - post_idx + 1
            root.left = build_subtree(pre_idx + 1, post_idx, temp_len_subtree)
            root.right = build_subtree(pre_idx + temp_len_subtree + 1, temp_post_idx + 1, len_subtree - temp_len_subtree - 1)

            return root

        dic_post = {}

        for idx, val in enumerate(post):
            dic_post[val] = idx

        return build_subtree(0, 0, len(pre))

        # if len(pre) == len(post) == 1:
        #     return TreeNode(pre[0])

        # self.roots = {}

        # def build_subtree(pre, post):
        #     dic_pre = {val: idx for idx, val in enumerate(pre)}
        #     dic_post = {val: idx for idx, val in enumerate(post)}
        #     len_pre = len(pre)
        #     len_post = len(post)
        #     temp_roots = {}
        #     pre_to_remove = []
        #     post_to_remove = []

        #     for val, pre_idx in dic_pre.items():
        #         post_idx = dic_post[val]

        #         if pre_idx + 1 < len_pre and post_idx - 1 > -1 and pre[pre_idx + 1] == post[post_idx - 1]:
        #             temp_val = pre[pre_idx + 1]
        #             temp_roots[temp_val] = TreeNode(temp_val)
        #             temp_roots[temp_val].left = self.roots[val] if val in self.roots else TreeNode(val)
        #             pre_to_remove.append(pre[pre_idx + 1])
        #             post_to_remove.append(post[post_idx - 1])
        #         elif pre_idx - 1 > -1 and post_idx + 1< len_post and pre[pre_idx - 1] == post[post_idx + 1]:
        #             temp_val = pre[pre_idx - 1]
        #             temp_roots[temp_val] = TreeNode(temp_val)
        #             temp_roots[temp_val].right = self.roots[val] if val in self.roots else TreeNode(val)
        #             pre_to_remove.append([pre_idx - 1])
        #             post_to_remove.append([post_idx + 1])
        #         elif pre_idx + 1 < len_pre and post_idx + 2 < len_post and pre_idx - 1 > -1 and pre[pre_idx + 1] == post[post_idx + 1] and pre[pre_idx - 1] == post[post_idx + 2]:
        #             temp_val = pre[pre_idx - 1]
        #             temp_left = pre[pre_idx]
        #             temp_right = pre[pre_idx + 1]
        #             temp_roots[temp_val] = TreeNode(temp_val)
        #             temp_roots[temp_val].left = self.roots[temp_left] if temp_left in self.roots else TreeNode(temp_left)
        #             temp_roots[temp_val].right = self.roots[temp_right] if temp_right in self.roots else TreeNode(temp_right)
        #             pre_to_remove.append(temp_left)
        #             pre_to_remove.append(temp_right)
        #             post_to_remove.append(temp_left)
        #             post_to_remove.append(temp_right)

        #     self.roots = temp_roots

        #     for num in pre_to_remove:
        #         pre.remove(num)

        #     for num in post_to_remove:
        #         post.remove(num)

        #     return pre, post

        # while len(pre) > 1 and len(post) > 1:
        #     pre, post = build_subtree(pre, post)

        # return list(self.roots.values())[0]


sol = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
# pre = [1]
# post = [1]
root = sol.constructFromPrePost(pre, post)

queue = [root]

while queue:
    print([node.val for node in queue])
    temp_queue = []

    for node in queue:
        if node.left:
            temp_queue.append(node.left)

        if node.right:
            temp_queue.append(node.right)

    queue = temp_queue
        