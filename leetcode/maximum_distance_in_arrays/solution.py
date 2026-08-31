class Solution:
    # Time: O(m) where m = len(arrays)
    # Space: O(1)
    def max_distance(self, arrays: list[list[int]]) -> int:
        result = 0
        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            # Pair the current array against the best extremes seen so far;
            # avoids using two extremes from the same array.
            result = max(result, arr[-1] - cur_min, cur_max - arr[0])
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])
        return result
