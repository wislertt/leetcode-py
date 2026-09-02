import random


class RandomizedCollection:
    # Time: insert O(1), remove O(1), get_random O(1) average
    # Space: O(n)
    def __init__(self) -> None:
        self.vals: list[int] = []
        self.positions: dict[int, set[int]] = {}

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        self.positions.setdefault(val, set()).add(len(self.vals) - 1)
        return len(self.positions[val]) == 1

    def remove(self, val: int) -> bool:
        indices = self.positions.get(val)
        if not indices:
            return False
        idx = indices.pop()
        last = len(self.vals) - 1
        last_val = self.vals[last]
        self.vals[idx] = last_val
        self.positions[last_val].add(idx)
        self.positions[last_val].discard(last)
        self.vals.pop()
        if not self.positions[val]:
            del self.positions[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.vals)
