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
            dict = {}
            for num in nums:
                if num in dict:
                    return True
                else:
                    dict[num] = ''
            
            return False
        else:
            return False