class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted copy
    def min_increment_for_unique(self, nums: list[int]) -> int:
        moves = 0
        previous = -1
        for num in sorted(nums):
            if num <= previous:
                # Raise num to one above the last placed value
                moves += previous - num + 1
                previous += 1
            else:
                previous = num
        return moves
