class Solution:
    def bulbSwitch(self, n: int) -> int:
        bound = 1 << n
        bulbs = bound - 1
        curr = 1
        res = 0
        
        for step in range(2, n + 1):
            toggle = bound >> step
            
            while toggle > 0:
                bulbs ^= toggle
                toggle >>= step
        
        while curr < bound:
            if curr & bulbs:
                res += 1
            
            curr <<= 1
        
        return res


sol = Solution()
print(sol.bulbSwitch(3))
