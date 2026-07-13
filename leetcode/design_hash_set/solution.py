class MyHashSet:
    # Time: O(1)
    # Space: O(n)
    def __init__(self) -> None:
        # Problem guarantees 0 <= key <= 10^6; a direct-address table is simplest.
        self._present: list[bool] = [False] * 1_000_001

    # Time: O(1)
    # Space: O(1)
    def add(self, key: int) -> None:
        self._present[key] = True

    # Time: O(1)
    # Space: O(1)
    def remove(self, key: int) -> None:
        self._present[key] = False

    # Time: O(1)
    # Space: O(1)
    def contains(self, key: int) -> bool:
        return self._present[key]
