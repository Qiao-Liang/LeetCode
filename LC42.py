class Solution(object):
    def trap_old(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        max_hgt = max(height)
        length = len(height)
        result = length * max_hgt
        left = 0
        right = length - 1

        while height[left] < max_hgt:
            left += 1
        
        while height[right] < max_hgt:
            right -= 1

        curr = 0
        last = 0
        while curr < left:
            if height[curr] > last:
                last = height[curr]

            result -= (max_hgt - last + height[curr])
            curr += 1

        curr = length - 1
        last = 0
        while curr > right:
            if height[curr] > last:
                last = height[curr]
            
            result -= (max_hgt - last + height[curr])
            curr -= 1

        for val in height[left: right + 1]:
            result -= val

        return result

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        left = 0 
        right = len(height) - 1
        max_left = height[0]
        max_right = height[-1]
        result = 0

        while left <= right:
            if height[left] < height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    result += (max_left - height[left])
                
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    result += (max_right - height[right])
                
                right -= 1

        return result
            



nums = [0,1,0,2,1,0,1,3,2,1,2,1]
# nums = [3, 1, 2, 1, 3]

sol = Solution()
print(sol.trap(nums))
