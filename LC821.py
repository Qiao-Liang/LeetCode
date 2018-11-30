class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indices = []
        res = [0] * len(S)

        for idx, ch in enumerate(S):
            if ch == C:
                indices.append(idx)

        dist = indices[0]
        for idx in xrange(indices[0]):
            res[idx] = dist
            dist -= 1

        for idx in xrange(1, len(indices)):
            left = indices[idx - 1]
            right = indices[idx]
            mid = (left + right) / 2
            dist = right - left
            res[mid] = dist / 2
            temp_left = mid - 1
            temp_right = mid + 1

            while temp_left > left:
                res[temp_left] = res[temp_left + 1] - 1
                temp_left -= 1
            
            if dist & 1:
                res[mid + 1] = res[mid]
                temp_right += 1

            while temp_right < right:
                res[temp_right] = res[temp_right - 1] - 1
                temp_right += 1

        dist = 1
        for idx in xrange(indices[-1] + 1, len(S)):
            res[idx] = dist
            dist += 1

        return res


sol = Solution()
# S = "loveleetcode"
# C = 'e'
S = "cizokxcijwbyspcfcqws"
C = "c"
print sol.shortestToChar(S, C)
