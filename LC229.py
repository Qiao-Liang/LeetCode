class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b, ca, cb = 0, 0, 0, 0

        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
            elif ca == 0:
                a, ca = num, 1
            elif cb == 0:
                b, cb = num, 1
            else:
                ca -= 1
                cb -= 1
            
        result = []
        len_nums = len(nums)
        for num in [a, b]:
            c = nums.count(num)
            if  c > len_nums / 3 and num not in result:
                result.append(num)
        
        return result


nums = [1, 1, 2, 1, 2, 3, 2, 2, 1]
sol = Solution()
print(sol.majorityElement([0, 0, 0]))
