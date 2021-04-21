class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        
        return len(diff) == 0 or (len(diff) == 2 and diff[0] == diff[1][::-1])


sol = Solution()
s1 = "ysmpagrkzsmmzmsssutzgpxrmoylkgemgfcperptsxjcsgojwourhxlhqkxumonfgrczmjvbhwvhpnocz"
s2 = "ysmpagrqzsmmzmsssutzgpxrmoylkgemgfcperptsxjcsgojwourhxlhkkxumonfgrczmjvbhwvhpnocz"
print(sol.areAlmostEqual(s1, s2))
