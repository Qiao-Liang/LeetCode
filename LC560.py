class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        curr_sum = 0
        right = 0
        left = 0
        nums_len = len(nums)

        while right < nums_len:
            if nums[right] == 0:
                count += 1
                right += 1
            elif nums[right] == k:
                count += 1
                left = right
                right += 1
            elif nums[right] > k:
                right += 1
                left = right
                curr_sum = 0
            else:
                curr_sum += nums[right]

                if curr_sum < k:
                    right += 1
                elif curr_sum > k:
                    while curr_sum > k and left < right:
                        curr_sum -= nums[left]
                        left += 1
                    
                    if curr_sum > k:
                        curr_sum = 0
                        right += 1
                        left = right
                else:
                    count += 1

                    while nums[left] == 0:
                        count += 1
                        left += 1

                    curr_sum -= nums[left]
                    left += 1
                    right += 1
        
        return count

sol = Solution()
# nums = [1,1,0,1,1,0,0,1,1]
# k = 2
nums = [-1, -1, 1]
k = 0

print(sol.subarraySum(nums, k))
