class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        left = list(dominoes)
        right = list(dominoes)
        len_dom = len(dominoes)
        res = ['.'] * len_dom
        
        for idx in range(1, len_dom):
            if left[idx] == '.' and left[idx - 1] == 'R':
                left[idx] = 'R'
        
        for idx in range(len_dom - 2, -1, -1):
            if right[idx] == '.' and right[idx + 1] == 'L':
                right[idx] = 'L'
        
        idx = 0

        while idx < len_dom:
            if left[idx] == 'R' and right[idx] != 'L':
                res[idx] = 'R'
                idx += 1
            elif right[idx] == 'L' and left[idx] != 'R':
                res[idx] = 'L'
                idx += 1
            elif right[idx] == left[idx] == '.':
                idx += 1
            else:
                temp_len = 0
                start = idx

                while idx < len_dom and left[idx] == 'R' and right[idx] == 'L':
                    idx += 1
                    temp_len += 1

                temp_len //= 2
                temp_count = temp_len
                temp_idx = start
                
                while temp_count > 0:
                    res[temp_idx] = 'R'
                    temp_idx += 1
                    temp_count -= 1

                temp_idx = idx - 1
                temp_count = temp_len

                while temp_count > 0:
                    res[temp_idx] = 'L'
                    temp_idx -= 1
                    temp_count -= 1
        
        return ''.join(res)


sol = Solution()
dom = ".L.R...LR..L.."
print(sol.pushDominoes(dom))

# LL.RR.LLRRLL..
# LL.RR.LLRRLL..
