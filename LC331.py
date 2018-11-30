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
