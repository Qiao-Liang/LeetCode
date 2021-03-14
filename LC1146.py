# from collections import OrderedDict
# from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = -1
        self.snaps = {}

    def set(self, index: int, val: int) -> None:
        self.snaps[(index, self.snap_id + 1)] = val
    
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        while snap_id > -1:
            if (index, snap_id) in self.snaps:
                return self.snaps[(index, snap_id)]

            snap_id -= 1

        return 0

    # def __init__(self, length: int):
    #     self.arr = [0] * length
    #     self.snaps = [OrderedDict() for _ in range(length)]
    #     self.snap_id = -1
    #     self.last_set = [None] * length

    # def set(self, index: int, val: int) -> None:
    #     self.arr[index] = val
    #     self.last_set[index] = val

    # def snap(self) -> int:
    #     self.snap_id += 1

    #     for i, v in enumerate(self.last_set):
    #         if v:
    #             self.snaps[i][self.snap_id] = v
    #             self.last_set[i] = None

    #     return self.snap_id

    # def get(self, index: int, snap_id: int) -> int:
    #     snaps = self.snaps[index]

    #     if snap_id in snaps:
    #         return snaps[snap_id]
    #     else:
    #         snap_keys = list(snaps.keys())

    #         if snap_keys:
    #             i = bisect_right(snap_keys, snap_id)
    #             return 0 if i == 0 else snaps[snap_keys[i - 1]]
    #         else:
    #             return 0


s = SnapshotArray(4)
s.set(1, 5)
s.snap()
s.set(0, 16)
s.snap()
s.set(2, 15)
s.snap()
s.set(2, 5)
print(s.get(1, 0))
print(s.get(0, 2))
s.snap()
