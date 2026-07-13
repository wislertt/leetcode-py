class FreqStack:
    def __init__(self) -> None:
        self.freq: dict[int, int] = {}
        self.group: dict[int, list[int]] = {}
        self.max_freq = 0

    # Time: O(1)
    # Space: O(n)
    def push(self, val: int) -> None:
        count = self.freq.get(val, 0) + 1
        self.freq[val] = count
        if count > self.max_freq:
            self.max_freq = count
        self.group.setdefault(count, []).append(val)

    # Time: O(1)
    # Space: O(n)
    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
