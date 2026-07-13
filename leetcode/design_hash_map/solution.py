class MyHashMap:
    # Time: O(n) init, O(1) ops
    # Space: O(n)
    def __init__(self) -> None:
        # Problem guarantees 0 <= key, value <= 10^6; -1 marks "no mapping".
        self._values: list[int] = [-1] * 1_000_001

    # Time: O(1)
    # Space: O(1)
    def put(self, key: int, value: int) -> None:
        self._values[key] = value

    # Time: O(1)
    # Space: O(1)
    def get(self, key: int) -> int:
        return self._values[key]

    # Time: O(1)
    # Space: O(1)
    def remove(self, key: int) -> None:
        self._values[key] = -1
