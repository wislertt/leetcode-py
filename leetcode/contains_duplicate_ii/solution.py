class Solution:
    # Time: O(n)
    # Space: O(n)
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        last_seen: dict[int, int] = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i

        return False
