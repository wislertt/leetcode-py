class Solution:
    # Time: O(len(nums))
    # Space: O(len(nums))
    def number_of_subarrays(self, nums: list[int], k: int) -> int:
        prefix: dict[int, int] = {0: 1}
        odds = 0
        count = 0
        for num in nums:
            odds += num % 2
            count += prefix.get(odds - k, 0)
            prefix[odds] = prefix.get(odds, 0) + 1
        return count
