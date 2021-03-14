class Solution:
    def findDiagonalOrder(self, nums):
        res = []
        q = [(0, 0)]
        rows = len(nums)
        
        while q:
            tq = []
            r, c = q[0]

            if r + 1 < rows and c < len(nums[r + 1]):
                tq.append((r + 1, c))
            
            for r, c in q:
                res.append(nums[r][c])
                cols = len(nums[r])
                
                if c + 1 < cols:
                    tq.append((r, c + 1))
            
            q = tq
        
        return res


sol = Solution()
# nums = [[1,2,3],[4,5,6],[7,8,9]]
# nums = [[1,2,3,4,5,6],[7]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
print(sol.findDiagonalOrder(nums))
