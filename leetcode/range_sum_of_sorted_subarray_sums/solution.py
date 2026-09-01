class Solution:
    # Time: O(n * log(sum(nums))) ~ O(n log n)
    # Space: O(1)
    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
        mod = 1_000_000_007

        def count_and_sum(target: int) -> tuple[int, int]:
            # Number of subarrays with sum <= target, plus the sum of those sums.
            count = 0
            total = 0
            window_sum = 0
            window_total = 0
            start = 0
            for end, value in enumerate(nums):
                window_sum += value
                window_total += value * (end - start + 1)
                while window_sum > target:
                    window_total -= window_sum
                    window_sum -= nums[start]
                    start += 1
                count += end - start + 1
                total += window_total
            return count, total

        def prefix_sum_of_sums(k: int) -> int:
            # Sum of the k smallest subarray sums.
            lo, hi = min(nums), sum(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                count, _ = count_and_sum(mid)
                if count < k:
                    lo = mid + 1
                else:
                    hi = mid
            count, total = count_and_sum(lo)
            return total - lo * (count - k)

        return (prefix_sum_of_sums(right) - prefix_sum_of_sums(left - 1)) % mod
