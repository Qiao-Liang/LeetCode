class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people:
            return 0

        people.sort()
        low = 0
        high = len(people) - 1
        res = 0

        while low < high:
            res += 1
            if people[low] + people[high] > limit:
                high -= 1
            else:
                low += 1
                high -= 1

        if low == high:
            res += 1

        return res

        # dic_weight_count = {}
        # res = 0

        # for weight in people:
        #     if weight in dic_weight_count:
        #         dic_weight_count[weight] += 1
        #     else:
        #         dic_weight_count[weight] = 1

        # weight_list = sorted(dic_weight_count.keys())
        # len_weight = len(weight_list)

        # for idx, weight in enumerate(weight_list):
        #     target = limit - weight
        #     left = idx
        #     right = len_weight
        #     not_found = True

        #     while left < right:
        #         mid = (left + right) // 2

        #         if weight_list[mid] > target:
        #             right = mid - 1
        #         elif weight_list[mid] < target:
        #             left = mid + 1
        #         else:
        #             not_found = False
        #             break

        #     if not_found:
        #         target = min(weight_list[left], weight_list[right])

        #     if dic_weight_count[target] == 0 or weight + target > limit:
        #         res += dic_weight_count[weight]
        #         dic_weight_count[weight] = 0
        #     else:
        #         while dic_weight_count[weight] > 0 and dic_weight_count[target] > 0:
        #             res += 1
        #             dic_weight_count[weight] -= 1
        #             dic_weight_count[target] -= 1

        # return res


sol = Solution()
people = [3,2,2,1]
limit = 3
# people = [3,5,3,4]
# limit = 5
# people = [2, 2]
# limit = 6
print(sol.numRescueBoats(people, limit))
        