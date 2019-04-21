class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        pre_list = preorder.split(',')
        count = 1

        for node in pre_list:
            if count == 0:
                return False

            if node == '#':
                count -= 1
            else:
                count += 1

        return count == 0


        # stack = []
        # node_list = preorder.split(',')
        
        # for node in node_list:
        #     if len(stack) == 1 and stack[0] == '#':
        #         return False

        #     stack.append(node)
            
        #     while len(stack) > 2 and stack[-1] == stack[-2] == '#':
        #         stack.pop()
        #         stack.pop()
        #         stack[-1] = '#'
                
        # return len(stack) == 1 and stack[0] == '#'
