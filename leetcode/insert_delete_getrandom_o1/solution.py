import random


class RandomizedSet:
    # List stores values; dict maps value -> index in list.
    # O(1) remove via swap-with-last trick: move last element into removed slot.
    # Time: O(1) average per operation
    # Space: O(n)
    def __init__(self) -> None:
        self.values: list[int] = []
        self.index: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        last_val = self.values[-1]
        remove_idx = self.index[val]
        # Move last element into the removed slot, then drop the tail
        self.values[remove_idx] = last_val
        self.index[last_val] = remove_idx
        self.values.pop()
        del self.index[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.values)
