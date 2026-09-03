class Solution:
    # Time: O(n^2 * k)
    # Space: O(n)
    def largest_sum_of_averages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        prefix = [0.0] * (n + 1)
        for i, value in enumerate(nums):
            prefix[i + 1] = prefix[i] + value

        def average(i: int, j: int) -> float:
            return (prefix[j] - prefix[i]) / (j - i)

        # best[i] = best score achievable for nums[i:] with the parts still available;
        # index n is the empty suffix, worth 0
        best = [average(i, n) for i in range(n)] + [0.0]
        for _ in range(2, k + 1):
            # ascending so best[end] still holds the (parts - 1) values
            for i in range(n):
                best[i] = max(average(i, end) + best[end] for end in range(i + 1, n + 1))
        return best[0]
