class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_lucky(self, arr: list[int]) -> int:
        counts: dict[int, int] = {}
        for value in arr:
            counts[value] = counts.get(value, 0) + 1
        result = -1
        for value, count in counts.items():
            if value == count:
                result = max(result, value)
        return result
