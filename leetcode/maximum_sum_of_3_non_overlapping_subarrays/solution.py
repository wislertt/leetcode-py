class Solution:
    # Time: O(n)
    # Space: O(n)
    def max_sum_of_three_subarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        window_count = n - k + 1
        sums = [sum(nums[:k])] + [0] * (window_count - 1)
        for i in range(k, n):
            sums[i - k + 1] = sums[i - k] + nums[i] - nums[i - k]

        # prefix_best[i]: earliest window in [0, i] with the max sum
        prefix_best = [(0, -1)] * window_count
        for i in range(window_count):
            if i == 0 or sums[i] > prefix_best[i - 1][0]:
                prefix_best[i] = (sums[i], i)
            else:
                prefix_best[i] = prefix_best[i - 1]

        # suffix_best[i]: earliest window in [i, end] with the max sum
        suffix_best = [(0, -1)] * window_count
        for i in range(window_count - 1, -1, -1):
            if i == window_count - 1 or suffix_best[i + 1][0] <= sums[i]:
                suffix_best[i] = (sums[i], i)
            else:
                suffix_best[i] = suffix_best[i + 1]

        best_total = -1
        result: list[int] = []
        for middle in range(k, window_count - k):
            total = prefix_best[middle - k][0] + sums[middle] + suffix_best[middle + k][0]
            if total > best_total:
                best_total = total
                result = [prefix_best[middle - k][1], middle, suffix_best[middle + k][1]]
        return result
