class Solution:
    # Time: O(n)
    # Space: O(n)
    def maximum_gap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        low, high = min(nums), max(nums)
        if low == high:
            return 0

        # Pigeonhole: the answer is at least ceil((high - low) / (n - 1)),
        # so buckets narrower than that guarantee the max gap spans buckets.
        size = max(1, (high - low) // (n - 1))
        count = (high - low) // size + 1
        bucket_min: list[int | None] = [None] * count
        bucket_max: list[int | None] = [None] * count

        for num in nums:
            idx = (num - low) // size
            lo = bucket_min[idx]
            hi = bucket_max[idx]
            if lo is None or hi is None:
                bucket_min[idx] = num
                bucket_max[idx] = num
            elif num < lo:
                bucket_min[idx] = num
            elif num > hi:
                bucket_max[idx] = num

        result = 0
        prev_max = low
        for idx in range(count):
            cur_min = bucket_min[idx]
            cur_max = bucket_max[idx]
            if cur_min is None or cur_max is None:
                continue
            result = max(result, cur_min - prev_max)
            prev_max = cur_max
        return result
