class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_list = [int(x) for x in str(n)]
        prev = -1
        pivot = len(n_list) - 1

        # Searches for the pivot (the first digit that is 
        # larger than the one next to it in the right)
        while pivot >= 0:
            if n_list[pivot] < prev:
                break
            else:
                prev = n_list[pivot]
                
            pivot -= 1

        if pivot == -1:
            return -1
        
        # Sorts the digits to the right of the pivot, 
        # searches for the first one that is larger than 
        # the pivot and swap it with the pivot 
        pivot_num = n_list[pivot]
        swap = len(n_list) - 1
        while swap > pivot:
            if n_list[swap] > pivot_num:
                n_list[pivot], n_list[swap] = n_list[swap], n_list[pivot]
                break
            
            swap -= 1

        result = int(''.join([str(n) for n in (n_list[:pivot + 1] + n_list[pivot + 1:][::-1])]))

        # Checks if the result is larger than the max 
        # of signed 32 bit (2 ** 31 - 1 = 2147483647)
        if result > 2147483647:
            return -1
        else:
            return result

sol = Solution()
print(sol.nextGreaterElement(12443322))