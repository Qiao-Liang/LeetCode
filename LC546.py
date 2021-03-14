class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        memo = {}
        li = len(boxes) - 1
        
        def recurse(s, e):
            if s > li or e < 0 or s > e:
                return 0
            
            if (s, e) in memo:
                return memo[s, e]
            else:
                i = s
                temp = 0

                while i <= e:
                    ti = i + 1
                    
                    while ti <= e and boxes[ti] == boxes[i]:
                        ti += 1
                    
                    memo[i, ti - 1] = (ti - i) ** 2
                    temp = max(temp, recurse(s, i - 1) + memo[i, ti - 1] + recurse(ti, e))
                    i = ti
                
                memo[s, e] = temp
                return temp
        
        temp = recurse(0, li)
        return temp

        # n = len(boxes)

        # mem = {}
        # for srt in range(n):
        #     mem[srt] = {}
        #     for end in range(srt, n):
        #         if srt == end:
        #             mem[srt][end] = 1
        #         else:
        #             mem[srt][end] = 0
        
        # def opt(srt, end):
        #     if mem.get(srt) and mem.get(srt).get(end):
        #         return mem.get(srt).get(end)
        #     else:
                

sol = Solution()
boxes = [1,3,2,2,2,3,4,3,1]
print(sol.removeBoxes(boxes))