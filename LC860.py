class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bill_counts = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 5:
                bill_counts[5] += 1
            elif bill == 10:
                if bill_counts[5] > 0:
                    bill_counts[5] -= 1
                    bill_counts[10] += 1
                else:
                    return False
            elif bill == 20:
                if bill_counts[10] > 0 and bill_counts[5] > 0:
                    bill_counts[5] -= 1
                    bill_counts[10] -= 1
                    bill_counts[20] += 1
                elif bill_counts[5] > 2:
                    bill_counts[5] -= 3
                    bill_counts[20] += 1
                else:
                    return False

        return True


sol = Solution()
bills = [5,5,5,10,20]
# bills = [5,5,10,10,20]
print(sol.lemonadeChange(bills))
