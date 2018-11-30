from sys import maxint

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        accu_remain = 0
        start_idx = 0
        min_remain = maxint
        len_gas = len(gas)

        for idx in xrange(len_gas):
            accu_remain += gas[idx] - cost[idx]

            if (accu_remain < min_remain):
                min_remain = accu_remain
                start_idx = (idx + 1) % len_gas

        if (accu_remain < 0):
            return -1
        else:
            return start_idx


    def canCompleteCircuit2(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum_gas = sum(gas)
        sum_cost = sum(cost)

        if sum_gas < sum_cost:
            return -1

        dest_dic = {}
        remain_dic = {}
        starts = []
        len_cir = len(gas)

        for idx in xrange(len_cir):
            if gas[idx] >= cost[idx]:
                starts.append(idx)

        for idx in starts:
            counter = len_cir
            curr = idx
            curr_gas = 0

            while counter:
                if curr in dest_dic:
                    curr_gas += remain_dic[curr]

                    if dest_dic[curr] > curr:
                        counter -= (dest_dic[curr] - curr)
                    else:
                        counter -= (len_cir - curr + dest_dic[curr])

                    curr = dest_dic[curr]
                else:
                    curr_gas += gas[curr]
                    
                    if curr_gas >= cost[curr]:
                        curr_gas -= cost[curr]
                        curr = (curr + 1) % len_cir
                        counter -= 1
                    else:
                        dest_dic[idx] = curr
                        remain_dic[idx] = curr_gas
                        break

            if counter == 0:
                return idx

        return -1


sol = Solution()
# gas  = [1,2,3,4,5] #[4, 5, 1, 2, 3]
# cost = [3,4,5,1,2] #[1, 2, 3, 4, 5]
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
# gas = [3, 3, 4]
# cost = [3, 4, 4]
print sol.canCompleteCircuit(gas, cost)
