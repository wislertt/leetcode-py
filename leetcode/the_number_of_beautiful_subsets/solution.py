class Solution:
    # Time: O(n log n + n)
    # Space: O(n)
    def beautiful_subsets(self, nums: list[int], k: int) -> int:
        freq: dict[int, int] = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        total = 1
        for residue in {num % k for num in nums}:
            vals = sorted(v for v in freq if v % k == residue)
            # f = valid subsets over values seen so far (empty included);
            # f_prev2 = same, excluding the most recent value.
            f, f_prev2, prev = 1, 0, None
            for val in vals:
                if prev is not None and val - prev == k:
                    # Cannot pick both val and prev.
                    f, f_prev2 = ((1 << freq[val]) - 1) * f_prev2 + f, f
                else:
                    f, f_prev2 = (1 << freq[val]) * f, f
                prev = val
            total *= f
        return total - 1
