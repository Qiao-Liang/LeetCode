class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return max(rec1[2], rec2[2]) - min(rec1[0], rec2[0]) < rec1[2] - rec1[0] + rec2[2] - rec2[0] and max(rec1[3], rec2[3]) - min(rec1[1], rec2[1]) < rec1[3] - rec1[1] + rec2[3] - rec2[1]

        
sol = Solution()
# rec1 = [0,0,2,2]
# rec2 = [1,1,3,3]
# rec1 = [0,0,1,1]
# rec2 = [1,0,2,1]
# rec1 = [4,0,6,6]
# rec2 = [-5,-3,4,2]
rec1 = [2,17,6,20]
rec2 = [3,8,6,20]
print sol.isRectangleOverlap(rec1, rec2)
