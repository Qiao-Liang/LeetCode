class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = xor0 = xor1 = 0

        for num in range(1, len(nums) + 1):
            xor ^= num

        for num in nums:
            xor ^= num

        rightmost_bit = xor & -xor

        for num in range(1, len(nums) + 1):
            if num & rightmost_bit:
                xor1 ^= num
            else:
                xor0 ^= num

        for num in nums:
            if num & rightmost_bit:
                xor1 ^= num
            else:
                xor0 ^= num
        
        for num in nums:
            if num == xor0:
                return [xor0, xor1]

        return [xor1, xor0]

        # if not nums:
        #     return None

        # stat = [0] * (len(nums) + 1)
        # result = [0, 0]

        # for n in nums:
        #     stat[n] += 1

        # for idx in range(1, len(stat)):
        #     if stat[idx] == 0:
        #         result[1] = idx
        #     if stat[idx] == 2:
        #         result[0] = idx

        # return result


sol = Solution()
nums = [1,2,2,4]
# nums = [1,3,3]
# nums = [8,7,3,5,3,6,1,4]
print(sol.findErrorNums(nums))
