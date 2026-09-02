class Solution:
    # Time: O(n * m) where n = len(arr), m = max value range span
    # Space: O(n)
    def transform_array(self, arr: list[int]) -> list[int]:
        result = arr[:]
        while True:
            prev = result[:]
            changed = False
            for i in range(1, len(prev) - 1):
                if prev[i] > prev[i - 1] and prev[i] > prev[i + 1]:
                    result[i] -= 1
                    changed = True
                elif prev[i] < prev[i - 1] and prev[i] < prev[i + 1]:
                    result[i] += 1
                    changed = True
            if not changed:
                return result
