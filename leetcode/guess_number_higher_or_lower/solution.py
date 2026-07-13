def guess(num: int) -> int:
    # Predefined by LeetCode; injected by tests.
    raise NotImplementedError


class Solution:
    # Time: O(log n)
    # Space: O(1)
    def guess_number(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result < 0:
                high = mid - 1
            else:
                low = mid + 1
        return -1
