"""
Contains Duplicate
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums:
            hash = set([])

            for num in nums:
                if num in hash:
                    return True
                else:
                    hash.add(num)
            
            return False
        else:
            return False

        # if nums:
        #     dict = {}
        #     for num in nums:
        #         if num in dict:
        #             return True
        #         else:
        #             dict[num] = ''
            
        #     return False
        # else:
        #     return False