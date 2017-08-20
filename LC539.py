class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        temp = map(lambda time:int(time[:2]) * 60 + int(time[3:]), timePoints)
        temp.sort()
        temp.append(temp[0] + 1440)  # Append the first element + 1440 to the end to simplify the circular difference
        min_diff = temp[1] - temp[0]

        for idx in range(1, len(temp)):
            diff = temp[idx] - temp[idx - 1]
            
            if diff < min_diff:
                min_diff = diff
        
        return min_diff

sol = Solution()
times = ["01:39","10:26","21:43"]
print(sol.findMinDifference(times))
