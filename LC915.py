class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = [(val, idx) for idx, val in enumerate(A)]
        temp.sort(key=lambda n: n[0])
        max_idx = -1
        idx_set = set([])
        
        for _, idx in temp:
            max_idx = max(max_idx, idx)
            idx_set.add(idx)
            
            if max_idx + 1 == len(idx_set):
                return max_idx + 1


sol = Solution()
a = [1,1,1,0,6,12]
# a = [1, 1]
# a = [90,47,69,10,43,92,31,73,61,97]
print(sol.partitionDisjoint(a))
