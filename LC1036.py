from collections import defaultdict

class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        blocked.sort(key=lambda n: (n[0], n[1]))
        bound = 10 ** 6
        dic_col_block = defaultdict(list)
        dic_row_block = defaultdict(list)

        if source[0] < target[0]:
            s_r = source[0]
            e_r = target[0]
        else:
            s_r = target[0]
            e_r = source[0]

        if source[1] < target[1]:
            s_c = source[1]
            e_c = target[1]
        else:
            s_c = target[1]
            e_c = source[1]
        
        for r, c in blocked:
            if s_r < r < e_r:
                dic_row_block[r].append(c)
            
            if s_c < c < e_c:
                dic_col_block[c].append(r)

        

