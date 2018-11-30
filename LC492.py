from math import ceil

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        result = [area, 1]
        min_diff = area - 1
        upper = area ** 0.5
        if upper.is_integer():
            upper += 1
        else:
            upper = ceil(upper)
        
        for length in xrange(1, int(upper)):
            if area % length == 0:
                width = area / length

                if width > length:
                    width, length = length, width

                if length - width < min_diff:
                    min_diff = length - width
                    result = [length, width]

        return result


sol = Solution()
print sol.constructRectangle(10)
