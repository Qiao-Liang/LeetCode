from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        count = Counter(arr)
        found = False
        
        for v in count.values():
            if v == 1:
                found = True
                break
            
        return found and len(set(count.values())) == len(count.keys())


sol = Solution()
# arr = [1,2,2,1,1,3]
# arr = [1, 2]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(sol.uniqueOccurrences(arr))
