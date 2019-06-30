class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        groups = {i: i for i in range(N)}
        remain = N - 1
        logs.sort(key=lambda n: n[0])

        def find(i):
            if i != groups[i]:
                groups[i] = find(groups[i])

            return groups[i]

        def union(x, y):
            tx = find(x)
            ty = find(y)

            if tx == ty:
                return 0
            else:
                groups[tx] = groups[ty]
                return 1

        for t, p1, p2 in logs:
            remain -= union(p1, p2)

            if remain == 0:
                return t
        
        return -1

        # groups = {}
        # logs.sort(key=lambda n:n[0])
        
        # for t, p1, p2 in logs:
        #     for key, value in groups.items():
        #         if key == p1:
        #             value.add(p2)
        #             break
        #         elif key == p2:
        #             value.add(p1)
        #             break
        #     else:
        #         groups[p1] = {p1, p2}
            
        #     keys = list(groups.keys())
        #     to_delete = set([])
            
        #     for idx, l in enumerate(keys):
        #         temp_item = groups[l]
                
        #         for r in keys[idx + 1:]:
        #             if r in temp_item or groups[l] & groups[r]:
        #                 temp_item.update(groups[r])
        #                 to_delete.add(r)

        #     for key in to_delete:
        #         del groups[key]
            
        #     if len(groups) == 1 and len(list(groups.values())[0]) == N:
        #         return t
            
        # return -1


sol = Solution()
# logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
# N = 6
# logs = [[3,1,4],[2,0,4],[8,2,4],[0,0,2],[5,4,3],[4,1,2],[10,0,2],[6,1,0],[7,4,0],[1,1,2],[9,1,3]]
# N = 5
# logs = [[3,0,3],[4,1,2],[0,2,0],[2,0,2],[8,0,3],[1,0,1],[5,1,2],[7,3,1],[6,1,0],[9,3,0]]
# N = 4
# logs = [[7,4,2],[0,2,0],[12,1,2],[10,5,1],[6,1,5],[11,5,4],[5,1,0],[3,1,2],[1,4,3],[9,1,3],[8,4,3],[2,1,0],[4,5,3]]
# N = 6
print(sol.earliestAcq(logs, N))
