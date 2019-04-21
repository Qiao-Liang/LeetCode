class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sum_A = sum(A)
        
        if sum_A % 3:
            return False
        
        temp = target = sum_A // 3
        count = 0
        
        for num in A:
            temp -= num
            
            if temp == 0:
                temp = target
                count += 1
        
        return count == 3
