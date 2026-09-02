from collections import Counter


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def find_least_num_of_unique_ints(self, arr: list[int], k: int) -> int:
        counts = sorted(Counter(arr).values())
        remaining = len(counts)
        for count in counts:
            if k < count:
                break
            k -= count
            remaining -= 1
        return remaining
