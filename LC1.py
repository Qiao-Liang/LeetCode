class Solution(object):
    def twoSum_Brute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None

        length = len(nums)
        for left in range(length):
            for right in range(left + 1, length):
                if nums[left] + nums[right] == target:
                    return [left, right]
        
        return None


    def twoSum_TwoPointer(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None

        head = 0
        tail = len(nums) - 1

        dict_nums = {}
        for idx, val in enumerate(nums):
            if val in dict_nums:
                dict_nums[val].append(idx)
            else:
                dict_nums[val] = [idx]

        nums = sorted(nums)

        while head < tail:
            temp = nums[head] + nums[tail]
            if temp == target:
                return [dict_nums[nums[head]].pop(0), dict_nums[nums[tail]].pop(0)]
            elif temp > target:
                tail -= 1
            elif temp < target:
                head += 1
        
        return None

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None

        dict_nums = {}
        for idx, val in enumerate(nums):
            temp = target - val
            if temp in dict_nums:
                return [dict_nums[temp], idx]

            dict_nums[val] = idx

        return None

sol = Solution()
nums = [2, 2, 4]
print(sol.twoSum(nums, 6))