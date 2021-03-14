class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        l = len(start)
        counts = {'R': 1, 'X': 0, 'L': -1}
        count = 0

        for i in range(l):
            diff = counts[start[i]] - counts[end[i]]
            count += diff

            if count < 0 or abs(diff) == 2:
                return False
        
        return count == 0
