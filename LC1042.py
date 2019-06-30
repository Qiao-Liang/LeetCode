from collections import defaultdict

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        self.ans = None
        self.res = [1] * (N + 1)
        self.found_res = False
        path_dic = defaultdict(list)
        
        for x, y in paths:
            path_dic[x].append(y)
            path_dic[y].append(x)

        self.keys = list(path_dic.keys())
        self.len_keys = len(self.keys)

        for key in self.keys:
            self.res[key] = None

        def recurse(idx):
            if self.found_res:
                return

            if idx == self.len_keys:
                self.found_res = True
                self.ans = self.res[:]
                return
            
            key = self.keys[idx]

            for flower in range(1, 5):
                can_plant = True

                for nei in path_dic[key]:
                    if self.res[nei] == flower:
                        can_plant = False
                
                if can_plant:
                    self.res[key] = flower
                    recurse(idx + 1)
                    self.res[key] = None
        
        recurse(0)
        return self.ans[1:]
        
        # def recurse(label, plants):
        #     if self.found_res:
        #         return

        #     if label > N:
        #         self.res = plants[:]
        #         self.found_res = True
        #         return
            
        #     for flower in range(1, N + 1):
        #         can_plant = True
                
        #         for nei in path_dic[label]:
        #             if plants[nei] == flower:
        #                 can_plant = False
                    
        #         if can_plant:
        #             plants[label] = flower
        #             recurse(label + 1, plants)
        #             plants[label] = None
        
        # recurse(1, [None] * (N + 1))
        # return self.res[1:]


sol = Solution()
N = 4
paths = [[1,2],[3,4]]
# N = 3
# paths = [[1,2],[2,3],[3,1]]
# paths = [[1, 2]]
# paths = []
print(sol.gardenNoAdj(N, paths))
