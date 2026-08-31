from bisect import bisect_left


class Solution:
    # Sort widths ascending (heights descending within equal widths), then the
    # answer is the longest strictly increasing subsequence of heights: patience
    # sorting with bisect_left keeps equal heights from chaining.
    # Time: O(n log n)
    # Space: O(n)
    def max_envelopes(self, envelopes: list[list[int]]) -> int:
        tails: list[int] = []
        for _, height in sorted(envelopes, key=lambda e: (e[0], -e[1])):
            index = bisect_left(tails, height)
            if index == len(tails):
                tails.append(height)
            else:
                tails[index] = height
        return len(tails)
