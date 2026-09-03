class Solution:
    # Time: O(n)
    # Space: O(1) auxiliary (slices are short, each of length part_len)
    def three_equal_parts(self, arr: list[int]) -> list[int]:
        total_ones = arr.count(1)
        if total_ones % 3 != 0:
            return [-1, -1]
        if total_ones == 0:
            return [0, len(arr) - 1]

        target = total_ones // 3
        marks: list[int] = []
        seen = 0
        for idx, bit in enumerate(arr):
            if bit == 1:
                seen += 1
                if seen in (1, target + 1, 2 * target + 1):
                    marks.append(idx)
        first, second, third = marks

        part_len = len(arr) - third
        if arr[first : first + part_len] != arr[third:]:
            return [-1, -1]
        if arr[second : second + part_len] != arr[third:]:
            return [-1, -1]
        return [first + part_len - 1, second + part_len]
