class Solution:
    def missingNumber(self, arr) -> int:
        if not arr:
            return None

        diffs = []
        diff = temp = None
        
        for i in range(1, len(arr)):
            diffs.append(arr[i] - arr[i - 1])
        
        temp, diff = max(diffs), min(diffs)

        if temp < 0 and diff < 0:
            temp, diff = diff, temp
        
        for i, v in enumerate(diffs):
            if v == temp:
                return arr[i] + diff


sol = Solution()
# a = [5, 7, 11, 13]
# a = [15, 13, 12, 11]
# a = [100,300,400]
a = [1,2,3,5]
print(sol.missingNumber(a))
