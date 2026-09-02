from bisect import bisect_left, bisect_right


class Solution:
    # Time: O(m log m + n log n + (m + n) log m), m = len(flowers), n = len(people)
    # Space: O(m)
    def full_bloom_flowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        starts = sorted(s for s, _ in flowers)
        ends = sorted(e for _, e in flowers)
        return [bisect_right(starts, t) - bisect_left(ends, t) for t in people]
