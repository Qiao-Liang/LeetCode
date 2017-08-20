class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)

        mem = {}
        for srt in range(n):
            mem[srt] = {}
            for end in range(srt, n):
                if srt == end:
                    mem[srt][end] = 1
                else:
                    mem[srt][end] = 0
        
        def opt(srt, end):
            if mem.get(srt) and mem.get(srt).get(end):
                return mem.get(srt).get(end)
            else:
                

# sol = Solution()
# boxes = [1,3,2,2,2,3,4,3,1]
# mem = sol.removeBoxes(boxes)