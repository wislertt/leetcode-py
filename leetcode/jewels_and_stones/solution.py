class Solution:
    # Time: O(n + m)
    # Space: O(n)
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(stone in jewel_set for stone in stones)
