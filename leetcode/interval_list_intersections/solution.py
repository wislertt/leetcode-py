class Solution:
    # Time: O(m + n)
    # Space: O(1) excluding output
    def interval_intersection(
        self, first_list: list[list[int]], second_list: list[list[int]]
    ) -> list[list[int]]:
        result: list[list[int]] = []
        i = j = 0
        while i < len(first_list) and j < len(second_list):
            lo = max(first_list[i][0], second_list[j][0])
            hi = min(first_list[i][1], second_list[j][1])
            if lo <= hi:
                result.append([lo, hi])
            if first_list[i][1] < second_list[j][1]:
                i += 1
            else:
                j += 1
        return result
