class ArrayReader:
    # Test-harness API: backs the compareSub/length interface with the array
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def compare_sub(self, lo1: int, hi1: int, lo2: int, hi2: int) -> int:
        left = sum(self.arr[lo1 : hi1 + 1])
        right = sum(self.arr[lo2 : hi2 + 1])
        return (left > right) - (left < right)

    def length(self) -> int:
        return len(self.arr)


class Solution:
    # Time: O(log n) compare_sub calls
    # Space: O(1)
    def get_index(self, reader: ArrayReader) -> int:
        left, right = 0, reader.length() - 1
        while left < right:
            # Split into two equal-size leading blocks plus a remainder block;
            # equal sizes guarantee a 0 result rules out both leading blocks.
            t2 = left + (right - left) // 3
            t3 = left + ((right - left) // 3) * 2 + 1
            cmp = reader.compare_sub(left, t2, t2 + 1, t3)
            if cmp == 0:
                left = t3 + 1
            elif cmp == 1:
                right = t2
            else:
                left, right = t2 + 1, t3
        return left
