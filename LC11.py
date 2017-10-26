class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        vol = 0

        while left < right:
            vol = max(vol, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return vol

sol = Solution()
height = [1,3,2,5,25,24,5]
print(sol.maxArea(height))
