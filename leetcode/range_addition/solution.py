class Solution:
    # Time: O(n + k) for k updates
    # Space: O(1) extra (excluding output)
    def get_modified_array(self, length: int, updates: list[list[int]]) -> list[int]:
        diff = [0] * (length + 1)
        for start, end, inc in updates:
            diff[start] += inc
            diff[end + 1] -= inc
        result = [0] * length
        running = 0
        for i in range(length):
            running += diff[i]
            result[i] = running
        return result
