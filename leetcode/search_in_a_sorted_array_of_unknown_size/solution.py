class ArrayReader:
    # Test-harness API: backs get() with the hidden sorted array
    def __init__(self, secret: list[int]) -> None:
        self.secret = secret

    def get(self, index: int) -> int:
        if 0 <= index < len(self.secret):
            return self.secret[index]
        return 2147483647


class Solution:
    # Time: O(log M), M = index of the target (bounds doubling then binary search)
    # Space: O(1)
    def search(self, reader: ArrayReader, target: int) -> int:
        # Grow the upper bound exponentially until get(right) >= target;
        # the out-of-bounds sentinel 2^31 - 1 is >= any valid target, so this
        # always terminates. The target, if present, lies in [right // 2, right].
        right = 1
        while reader.get(right) < target:
            right <<= 1
        left = right >> 1
        while left < right:
            mid = (left + right) >> 1
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid + 1
        return left if reader.get(left) == target else -1
