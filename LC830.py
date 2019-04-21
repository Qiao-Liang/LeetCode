class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        curr = ''
        g_idx = len_g = 0
        res = []
        
        for idx, ch in enumerate(S):
            if ch != curr:
                if len_g > 2:
                    res.append([g_idx, g_idx + len_g - 1])
                
                curr = ch
                g_idx = idx
                len_g = 1
            else:
                len_g += 1
        
        if len_g > 2:
            res.append([g_idx, g_idx + len_g - 1])
        
        return res    
