class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def intersection_size_two(self, intervals: list[list[int]]) -> int:
        # Sort by end ascending, start descending: later intervals shrink leftward,
        # so tracking the two largest chosen numbers suffices to test coverage.
        srt = sorted(intervals, key=lambda iv: (iv[1], -iv[0]))
        second_last = -1
        last = -1
        count = 0
        for start, end in srt:
            if start <= second_last:
                continue
            if start > last:
                count += 2
                second_last, last = end - 1, end
            else:
                count += 1
                second_last, last = last, end
        return count
