class Solution:
    # Time: O(log numBottles)
    # Space: O(1)
    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        drunk = num_bottles
        empty = num_bottles
        while empty >= num_exchange:
            full, empty = divmod(empty, num_exchange)
            drunk += full
            empty += full
        return drunk
