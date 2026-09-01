from bisect import bisect_left


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def minimum_mountain_removals(self, nums: list[int]) -> int:
        def lis_lengths(seq: list[int]) -> list[int]:
            tails: list[int] = []
            lengths: list[int] = []
            for x in seq:
                pos = bisect_left(tails, x)
                if pos == len(tails):
                    tails.append(x)
                else:
                    tails[pos] = x
                lengths.append(pos + 1)
            return lengths

        inc = lis_lengths(nums)
        dec = lis_lengths(nums[::-1])[::-1]

        best = 0
        for i in range(1, len(nums) - 1):
            if inc[i] >= 2 and dec[i] >= 2:
                best = max(best, inc[i] + dec[i] - 1)
        return len(nums) - best
