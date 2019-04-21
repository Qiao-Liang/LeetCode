class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        length = len(A)
        stay = 0
        swap = 1
        
        for idx in range(1, length):
            new_stay = new_swap = length

            if A[idx] > A[idx - 1] and B[idx] > B[idx - 1]:
                new_swap = swap + 1
                new_stay = stay
            
            if A[idx] > B[idx - 1] and B[idx] > A[idx - 1]:
                new_stay = min(new_stay, swap)
                new_swap = min(new_swap, stay + 1)

            swap = new_swap
            stay = new_stay

        return min(swap, stay)


        # length = len(A)
        # stay = [float('inf')] * length
        # swap = [float('inf')] * length
        # stay[0] = 0
        # swap[0] = 1
        
        # for idx in range(1, length):
        #     if A[idx] > A[idx - 1] and B[idx] > B[idx - 1]:
        #         stay[idx] = stay[idx - 1]
        #         swap[idx] = swap[idx - 1] + 1
            
        #     if A[idx] > B[idx - 1] and B[idx] > A[idx - 1]:
        #         stay[idx] = min(stay[idx], swap[idx - 1])
        #         swap[idx] = min(swap[idx], stay[idx - 1] + 1)
        
        # return min(stay[-1], swap[-1])


sol = Solution()
A = [1, 3, 5, 4]
B = [1, 2, 3, 7]
print(sol.minSwap(A, B))
