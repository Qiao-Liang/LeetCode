class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        poss = [nums[0]]

        for bound in nums[1:]:
            if bound < poss[0]:
                poss[0] = bound
            elif bound > poss[-1]:
                poss.append(bound)
            else:
                left = 0
                right = len(poss) - 1
                not_found = True

                while left < right:
                    mid = (left + right) / 2

                    if bound > poss[mid]:
                        left = mid + 1
                    elif bound < poss[mid]:
                        right = mid - 1
                    else:
                        not_found = False
                        break

                if not_found:
                    if bound < poss[right]:
                        poss[right] = bound
                    elif bound > poss[right]:
                        poss[right + 1] = bound

        return len(poss)


            # for idx in range(0, bound):
            #     if nums[idx] < nums[bound] and poss[idx] + 1 > poss[bound]:
            #         poss[bound] = poss[idx] + 1

        # return max(poss)


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
# nums = [4,10,4,3,8,9]
nums = [3,5,6,2,5,4,19,5,6,7,12]
sol = Solution()
print(sol.lengthOfLIS(nums))
