class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        def to_int(arr):
            pow = 0
            res = 0

            for d in reversed(arr):
                if d:
                    res += (-2) ** pow
                
                pow += 1

            return res

        def baseNeg2(N):
            if N == 0:
                return '0'
            
            res = ""

            while (N != 0): 
                remainder = N % (-2) 
                N //= -2 

                if (remainder < 0): 
                    remainder += (-1 * -2) 
                    N += 1
        
                res = str(remainder) + res 
                
            return res

        return baseNeg2(to_int(arr1) + to_int(arr2))


        # idx1 = len(arr1) - 1
        # idx2 = len(arr2) - 1
        # carry = 0
        # temp = []
        # power = 0
        # res = 0
        
        # while idx1 > -1 and idx2 > -1:
        #     temp.append(arr1[idx1] ^ arr2[idx2] ^ carry)
        #     carry = arr1[idx1] and arr2[idx2] or arr1[idx1] and carry or arr2[idx2] and carry
        #     idx1 -= 1
        #     idx2 -= 1
        
        # while idx1 > -1:
        #     temp.append(arr1[idx1] ^ carry)
        #     carry = carry and arr1[idx1]
        #     idx1 -= 1
        
        # while idx2 > -1:
        #     temp.append(arr2[idx2] ^ carry)
        #     carry = carry and arr2[idx2]
        #     idx2 -= 1
            
        # temp.reverse()
        # return temp


sol = Solution()
arr1 = [1,1,1,1,1]
arr2 = [1,0,1]
print(sol.addNegabinary(arr1, arr2))
