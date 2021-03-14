class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        count = [[0] * width for _ in range(height)]

        for r in range(height - sideLength + 1):
            for c in range(width - sideLength + 1):
                for ro in range(sideLength):
                    for co in range(sideLength):
                        count[r + ro][c + co] += 1

        print(count)


sol = Solution()
width = 100
height = 100
sideLength = 2
maxOnes = 2
sol.maximumNumberOfOnes(width, height, sideLength, maxOnes)
