class Solution:
    # Time: O(n)
    # Space: O(n)
    def distribute_candies(self, candy_type: list[int]) -> int:
        return min(len(set(candy_type)), len(candy_type) // 2)
