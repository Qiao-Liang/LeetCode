class Node(object):
    def __init__(self, sym, val=None):
        self.sym = sym
        self.val = val
        self.children = {}

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie_root = Node(None)

        for num in nums:
            temp = 1 << 31
            curr = trie_root

            while temp > 0:
                temp_val = 1 if temp & num else 0

                if temp_val in curr.children:
                    curr = curr.children[temp_val]
                else:
                    temp_node = Node(temp_val)
                    curr.children[temp_val] = temp_node
                    curr = temp_node

                temp >>= 1

            curr.val = num
        
        max_xor = 0

        for num in nums:
            temp = 1 << 31
            curr = trie_root
            temp_val = 0

            while curr.children:
                if len(curr.children) > 1:
                    curr = curr.children[0 if temp & num else 1]
                else:
                    curr = curr.children.items()[0][1]

                temp >>= 1

            max_xor = max(max_xor, curr.val ^ num)

        return max_xor


sol = Solution()
print sol.findMaximumXOR([3, 10, 5, 16, 25, 2, 8])
