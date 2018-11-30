class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]

        if old_color == newColor:
            return image

        stack = [(sr, sc)]
        rows = len(image)
        cols = len(image[0])

        while stack:
            r, c = stack[-1]
            image[r][c] = newColor

            if r > 0 and image[r - 1][c] == old_color:
                stack.append((r - 1, c))
                continue

            if r < rows - 1 and image[r + 1][c] == old_color:
                stack.append((r + 1, c))
                continue
            
            if c > 0 and image[r][c - 1] == old_color:
                stack.append((r, c - 1))
                continue

            if c < cols - 1 and image[r][c + 1] == old_color:
                stack.append((r, c + 1))
                continue

            stack.pop()
        
        return image


sol = Solution()
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# newColor = 2
image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
print(sol.floodFill(image, sr, sc, newColor))
