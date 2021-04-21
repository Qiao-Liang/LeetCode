class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        
        for i, c in enumerate(s):
            if c in dic:
                dic[c][1] = i
            else:
                dic[c] = [i, i]
                
        intervals = list(dic.values())
        intervals.sort(key=lambda n: n[0])
        prv = [intervals[0]]
        
        for s, e in intervals[1:]:
            if s < prv[-1][1]:
                prv[-1][1] = max(prv[-1][1], e)
            else:
                prv.append([s, e])
                
        return [e - s + 1 for s, e in prv]
