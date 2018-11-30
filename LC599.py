class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {}
        set2 = set(list2)

        for idx, val in enumerate(list1):
            if val in set2:
                dic[val] = idx

        for idx, val in enumerate(list2):
            if val in dic:
                dic[val] += idx

        min_idx = min([idx for (val, idx) in dic.items()])

        return [val for (val, idx) in dic.items() if idx == min_idx]


sol = Solution()
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
print(sol.findRestaurant(list1, list2))
