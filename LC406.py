class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []

        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(p[1], p)

        return res

        # sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        # res = []

        # for people in sorted_people:
        #     res.insert(people[1], people)

        # return res

        # res = []
        # count = {}

        # for item in people:
        #     if item[1] == 0:
        #         res.append(item)

        #         if item[0] in count:
        #             count[item[0]] += 1
        #         else:
        #             count[item[0]] = 1
        
        # res = sorted(res, key=lambda x: x[0])

        # for item in res:
        #     people.remove(item)

        # while len(people) > 0:
        #     temp_items = []

        #     for item in people:
        #         temp_count = 0

        #         for count_key in count.keys():
        #             if count_key >= item[0]:
        #                 temp_count += count[count_key]

        #         if item[1] == temp_count:
        #             temp_items.append(item)

        #     if temp_items:
        #         temp_item = sorted(temp_items, key=lambda x: (x[1], -x[0]))[-1]
        #         res.append(temp_item)

        #         if temp_item[0] in count:
        #             count[temp_item[0]] += 1
        #         else:
        #             count[temp_item[0]] = 1
                
        #         people.remove(temp_item)
                
        # return res
        

        # for item in people:
        #     if item[1] in dic:
        #         dic[item[1]].append(item)
        #     else:
        #         dic[item[1]] = [item]

        # for key in dic.keys():
        #     dic[key] = sorted(dic[key], key=lambda x: x[0])
        
        # res = dic[0]

        # while len(res) < len(people):
        #     if len(res) in dic:
        #         res.append(dic[len(res)].pop(0))
        #     else:
        #         for val in dic.values():
        #             count = 0
                    
        #             for item in res:
        #                 if item[0] >= val[0]:
        #                     count += 1

        #             if count == val[1]:
        #                 res.append(val)

        # return res


sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(sol.reconstructQueue(people))
