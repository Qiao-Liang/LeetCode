from datetime import date as dd

class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = list(map(int, date.split('-')))
        return (dd(y, m, d) - dd(y, 1, 1)).days + 1


sol = Solution()
d = "2019-01-09"
print(sol.dayOfYear(d))
