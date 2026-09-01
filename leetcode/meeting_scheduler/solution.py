class Solution:
    # Time: O(m log m + n log n)
    # Space: O(1) extra (in-place sorts)
    def min_available_duration(
        self, slots1: list[list[int]], slots2: list[list[int]], duration: int
    ) -> list[int]:
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
