class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        len_row = len(row)
        indices = [0] * len_row
        curr_idx = 0
        exc_count = 0

        for idx, val in enumerate(row):
            indices[val] = idx

        while curr_idx < len_row:
            value = row[curr_idx]

            if value & 1 == 0:
                if row[curr_idx + 1] - value != 1:
                    exc_val_0 = value + 1
                    exc_idx_0 = indices[exc_val_0]
                    exc_idx_1 = curr_idx + 1
                    exc_val_1 = row[exc_idx_1]

                    row[exc_idx_0], row[exc_idx_1] = row[exc_idx_1], row[exc_idx_0]
                    indices[exc_val_0], indices[exc_val_1] = indices[exc_val_1], indices[exc_val_0]
                    exc_count += 1
            else:
                if value - row[curr_idx + 1] != 1:
                    exc_val_0 = value - 1
                    exc_idx_0 = indices[exc_val_0]
                    exc_idx_1 = curr_idx + 1
                    exc_val_1 = row[exc_idx_1]

                    row[exc_idx_0], row[exc_idx_1] = row[exc_idx_1], row[exc_idx_0]
                    indices[exc_val_0], indices[exc_val_1] = indices[exc_val_1], indices[exc_val_0]
                    exc_count += 1

            curr_idx += 2

        return exc_count


sol = Solution()
# row = [0, 2, 1, 3]
# row = [3, 2, 0, 1]
# row = [0, 3, 2, 1]
row = [3, 5, 2, 0, 4, 1]
# row = [0, 2, 4, 6, 7, 1, 3, 5]

print(sol.minSwapsCouples(row))
